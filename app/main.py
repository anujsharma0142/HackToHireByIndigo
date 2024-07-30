import uvicorn
import time
import threading
from fastapi import FastAPI
from app.db.connector import database_manager
from app.kafka.kafka_consumer import KafkaFlightConsumer
from contextlib import asynccontextmanager
from config.config import get_server_config
from fastapi.middleware.cors import CORSMiddleware
from app.admin.routes import router as admin_router
import asyncio
from concurrent.futures import ThreadPoolExecutor


"""
    "Author": "Anuj Sharma",
    "email": "anujsharma0141@gmail.com"
"""

@asynccontextmanager
async def lifespan(app: FastAPI):
    consumer = KafkaFlightConsumer()
    loop = asyncio.get_running_loop()
    executor = ThreadPoolExecutor()
    loop.run_in_executor(executor, consumer.consume_messages)
    postgres = database_manager.get_database()
    await postgres.connect()
    yield
    await postgres.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(admin_router, prefix="/admin", tags=["admin"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.on_event("startup")
# def startup_event():
    # consumer = KafkaFlightConsumer()
    # consumer.consume_messages()

# def consume():
    
    
# async def consume():
#     threading.Thread(target=start_kafka_consumer, daemon=True).start()
# asyncio.run(consume())


@app.get("/")
async def read_root():
    return {"message": "Running Indego 6e"}


if __name__ == "__main__":
    config = get_server_config()
    uvicorn.run(app, host=config.get('host', '127.0.0.1'), port=int(config.get('port', 8000)), log_level="info")
