# Flask App

This is a simple Flask application that randomly displays GIFs of cats.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Docker (if you prefer to run the application in a container)

## How to Use Docker to Run the Application
Follow these steps to build and run the application using Docker:

1. Build the Docker Image
Navigate to your project directory and build the Docker image:

```bash
docker build -t flask-app .
```

2. Run the Docker Container
Run the Docker container with port forwarding:

```bash
docker run -p 8866:5000 flask-app
The application will be accessible at http://localhost:8866.
```

Project Structure
```plaintext
├── app.py               # Main Flask application file
├── requirements.txt     # List of Python dependencies
├── Dockerfile           # Dockerfile for building the Docker image
└── templates
    └── index.html       # HTML template for displaying the cat GIFs
```