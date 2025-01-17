# Text Similarity App

This is a Python-based application that compares two pieces of text to determine their semantic similarity using a pre-trained language model from Hugging Face. It includes the following additional features:

- Dockerized setup for easy deployment.
- MongoDB integration for storing user credentials (e.g., usernames and passwords).
- A REST API for interacting with the text similarity functionality.
- Hosted on GitHub for collaboration and version control.

## Features
- Compare any two texts and calculate their similarity score.
- Securely store usernames and passwords in a MongoDB database.
- Expose REST API endpoints for text similarity experimentation.
- Fully containerized for simple and reproducible deployment.

## Installation

### Prerequisites
- Docker
- Python 3.7+ (if running locally)
- pip (Python package manager, if running locally)

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/syntaxai-lab/textsimilarity_restapi.git
   cd textsimilarity_restapi
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
1. **Text Similarity Endpoint**
   - URL: `http://localhost:5000/similarity`
   - Method: POST
   - Payload:
     ```json
     {
       "text1": "How are you?",
       "text2": "What is your current state?"
     }
     ```
   - Response:
     ```json
     {
       "similarity_score": 0.85
     }
     ```

2. **User Registration Endpoint**
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
1. The app uses the `sentence-transformers` library to generate embeddings (numerical representations) for each input text.
2. Cosine similarity is calculated between the two embeddings to produce a similarity score ranging from -1 (completely dissimilar) to 1 (identical).
3. User data is securely stored in MongoDB, with endpoints for registration and authentication.

## File Structure
# Text Similarity App

This is a Python-based application that compares two pieces of text to determine their semantic similarity using a pre-trained language model from Hugging Face. It includes the following additional features:

- Dockerized setup for easy deployment.
- MongoDB integration for storing user credentials (e.g., usernames and passwords).
- A REST API for interacting with the text similarity functionality.
- Hosted on GitHub for collaboration and version control.

## Features
- Compare any two texts and calculate their similarity score.
- Securely store usernames and passwords in a MongoDB database.
- Expose REST API endpoints for text similarity experimentation.
- Fully containerized for simple and reproducible deployment.

## Installation

### Prerequisites
- Docker
- Python 3.7+ (if running locally)
- pip (Python package manager, if running locally)

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/text-similarity-app.git
   cd text-similarity-app
   ```

2. Build and run the Docker container:
   ```bash
   docker-compose up --build
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
1. **Text Similarity Endpoint**
   - URL: `http://localhost:5000/similarity`
   - Method: POST
   - Payload:
     ```json
     {
       "text1": "How are you?",
       "text2": "What is your current state?"
     }
     ```
   - Response:
     ```json
     {
       "similarity_score": 0.85
     }
     ```

2. **User Registration Endpoint**
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
1. The app uses the `sentence-transformers` library to generate embeddings (numerical representations) for each input text.
2. Cosine similarity is calculated between the two embeddings to produce a similarity score ranging from -1 (completely dissimilar) to 1 (identical).
3. User data is securely stored in MongoDB, with endpoints for registration and authentication.

## File Structure
```
textsimilarity_restapi/
├── app/                  # Application code
│   ├── app.py            # Main Flask application
│   ├── routes.py         # API route definitions
│   ├── models.py         # Database models
│   └── utils.py          # Utility functions
├── db/                   # MongoDB-related setup
│   ├── init.js           # MongoDB initialization script
│   └── docker-entrypoint-initdb.d/  # MongoDB entrypoint scripts
├── Dockerfile            # Docker configuration for the app
├── docker-compose.yml    # Docker Compose setup for app and MongoDB
├── requirements.txt      # Python dependencies
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

## Future Enhancements
- Add OAuth-based authentication for improved security.
- Extend support for additional similarity metrics.
- Deploy the app to a cloud platform (e.g., AWS, Azure, or Heroku).
- Add a frontend interface for user interaction.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to contribute or suggest improvements!