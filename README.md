# DB as a Service

This is a Python-based application that provides Database as a Service(DBaaS). It includes the following features:

- Dockerized setup for easy deployment.
- MongoDB integration for storing user credentials (e.g., usernames and passwords).
- A REST API for interacting with the DB.


## Features
- Securely store usernames and passwords in a MongoDB database.
- Uses Bcrypt to securely hash passwords before storing them
- Exposes REST API endpoints for interacting with the database and experimenting with data storage.
- Fully containerized for simple and reproducible deployment.

## Installation

### Prerequisites
- Docker (Docker Desktop or Docker Engine)

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/syntaxai-lab/mongodb_restapi.git
   cd mongodb_restapi
   ```

2. Build and run the Docker container:
   ```bash
   docker compose up --build
   ```
   This will set up the application and MongoDB.

## Usage
	Once the containers are running, test the API using Postman or cURL.

### REST API Endpoints
### REST API Endpoints
- `POST /register` – Register a new user
- `POST /login` – Authenticate a user
- `GET /users` – Retrieve a list of users *(coming soon)*

## How It Works
User data is securely stored in MongoDB, with endpoints for registration and authentication.

## File Structure
```
mongodb_restapi/
├── app/                  # Application code
│   ├── app.py            # Main Flask application
│   ├── Dockerfile        # Docker configuration for the app
│   └── requirements.txt  # Python dependencies
├── docker-compose.yml    # Docker Compose setup for app and MongoDB
├── README.md             # Project documentation
└── LICENSE               # License file
```

## Future Enhancements
- Add OAuth-based authentication for improved security.
- Extend support for additional similarity metrics.
- Deploy the app to a cloud platform (e.g., AWS, Azure, or Heroku).
- Add a frontend interface for user interaction.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to contribute or suggest improvements!
