# DB as a Service

This is a Python-based application that provides Database as a Service(DBaaS). It includes the following features:

- Dockerized setup for easy deployment.
- MongoDB integration for storing user credentials (e.g., usernames and passwords).
- A REST API for interacting with the DB.


## Features
- Securely store usernames and passwords in a MongoDB database.
- Expose REST API endpoints for experimentation, interacting with the DB and storage.
- Fully containerized for simple and reproducible deployment.

## Installation

### Prerequisites
- Docker
- Python 3.7+ (if running locally)
- pip (Python package manager, if running locally)

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

3. (Optional) Run locally without Docker:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python app.py
   ```

## Usage

### REST API Endpoints
1. **User Registration Endpoint**
   - URL: `http://localhost:5000/register`
   - Method: POST
   - Payload:
     ```json
     {
       "username": "test_user",
       "password": "secure_password"
     }
     ```
   - Response:
     ```json
     {
       "message": "User registered successfully."
     }
     ```

3. **User Login Endpoint**
   - URL: `http://localhost:5000/login`
   - Method: POST
   - Payload:
     ```json
     {
       "username": "test_user",
       "password": "secure_password"
     }
     ```
   - Response:
     ```json
     {
       "message": "Login successful."
     }
     ```



### Local Testing
Run the app locally and test the endpoints using a tool like Postman or cURL.

## How It Works
User data is securely stored in MongoDB, with endpoints for registration and authentication.

## File Structure
```
textsimilarity_restapi/
├── app/                  # Application code
│   ├── app.py            # Main Flask application
│   ├── Dockerfile        # Docker configuration for the app
│   └── requirements.txt  # Python dependencies
├── db/                   # MongoDB-related setup
│   ├── init.js           # MongoDB initialization script
│   └── docker-entrypoint-initdb.d/  # MongoDB entrypoint scripts
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
