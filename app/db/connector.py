from databases import Database
from config.config import get_database_config

class DatabaseManager:
    def __init__(self):
        self.db_config = get_database_config()
        self.database_url = f"postgresql://{self.db_config['user']}:{self.db_config['password']}@{self.db_config['host']}:{self.db_config['port']}/{self.db_config['database']}"
        self.database = Database(self.database_url)

    async def connect(self):
        if not self.database.is_connected:
            await self.database.connect()

    async def disconnect(self):
        if self.database.is_connected:
            await self.database.disconnect()

    def get_database(self):
        return self.database

# Singleton instance
database_manager = DatabaseManager()
