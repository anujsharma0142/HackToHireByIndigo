Here's an updated README file incorporating the provided configuration details:


Architecture Design 


![architect](https://github.com/user-attachments/assets/e3dc141b-f861-4db9-9ea1-938604a9aa3c)

# Flight Status and Notifications System - Backend

## Overview
This backend system provides real-time flight status updates and notifications to passengers. It is built using FastAPI, PostgreSQL, and Kafka, ensuring high performance, scalability, and reliability.

## Features
- Real-time flight status updates
- User subscription management
- Admin and user management
- Email notifications for flight status changes
- Integration with airport systems using mock data

## Technologies Used
- **FastAPI**: High-performance web framework for building APIs with Python.
- **PostgreSQL**: Reliable database for managing flight data and user information.
- **Kafka**: Message broker for real-time notifications.

## Installation

### Prerequisites
- Python 3.7+
- PostgreSQL
- Kafka

### Clone the Repository

git clone https://github.com/yourusername/flight-status-backend.git
cd flight-status-backend
```

### Install Dependencies
Create and activate a virtual environment, then install the required dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Configuration
Configure the application settings in the `config.ini` file:

```ini
[server]
host = 127.0.0.1
port = 8000

[database]
user = postgres
password = as0000
host = localhost
port = 5432
database = indigo_6e

[kafka]
bootstrap_host = 127.0.0.1
bootstrap_port = 9092
topic = flight_updates

[email]
service_email = ******@gmail.com
service_password = *****
smtp_host = smtp.gmail.com
smtp_port = 465
```

### Set Up PostgreSQL
Create a PostgreSQL database and ensure the connection settings in `config.ini` match your setup.

### Set Up Kafka
Ensure Kafka is running and the connection settings in `config.ini` match your setup.

### Run Database Migrations
Apply the database migrations to set up the database schema:

alembic upgrade head


## Usage

### Run the Application
Start the FastAPI server:
```bash
uvicorn main:app --reload
```

### API Endpoints

#### Admin Endpoints
- **Update Flight Status:** `POST /admin/update-flight-status`
- **Manage User Data:** `GET /admin/users`

#### User Endpoints
- **Subscribe to Flight Updates:** `POST /user/subscribe`
- **Get Flight Status:** `GET /user/flight-status/{flight_id}`

### Real-time Notifications
Kafka producers send real-time flight status updates, which are processed by Kafka consumers to trigger email notifications to passengers.

## Project Structure
```
flight-status-backend/
├── alembic/                  # Database migrations
├── app/
│   ├── api/                  # API endpoints
│   ├── core/                 # Core settings and configurations
│   ├── db/                   # Database models and schemas
│   ├── kafka/                # Kafka producers and consumers
│   ├── services/             # Business logic and services
│   ├── main.py               # Entry point for the application
├── tests/                    # Unit and integration tests
├── requirements.txt          # Python dependencies
├── config.ini                # Configuration file
├── README.md                 # Project documentation
```

## Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, please open an issue or contact the repository owner.

