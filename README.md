Chatbot Web Application

## Overview

This project is a web-based chatbot application built using Django and a machine learning model for natural language understanding and response generation. The chatbot is designed to interact with users through a web interface, providing relevant responses based on predefined intents and patterns.

## Features

- Natural Language Processing (NLP) for understanding user inputs.
- Predefined intents and patterns for generating appropriate responses.
- A user-friendly web interface for interacting with the chatbot.
- User authentication and session management.
- Scalable deployment on a cloud platform.

## ## Setup and Installation

### Prerequisites

- Python 3.8+
- PostgreSQL
- Virtualenv

### Installation Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/chatbot-project.git
   cd chatbot-project

   ```

2. **Set up a virtual environment:**

python3 -m venv venv
source venv/bin/activate

3. **Install the required packages:**

pip install -r requirements.txt

4. **Set up PostgreSQL database:**

Create a PostgreSQL database and user, and update chatbot_project/settings.py with your database credentials.

CREATE DATABASE chatbot_db;
CREATE USER your_db_user WITH PASSWORD 'your_db_password';
ALTER ROLE your_db_user SET client_encoding TO 'utf8';
ALTER ROLE your_db_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE your_db_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE chatbot_db TO your_db_user;

5. **Apply database migrations:**

python manage.py migrate

6. **Train the chatbot model:**

python train_chatbot.py

7. **Run the Django development server:**

python manage.py runserver

8. **Access the application:**

Open your web browser and go to http://127.0.0.1:8000.

---

Deployment

## To deploy the application using Nginx and Gunicorn, follow these steps:

1. **Run the deployment script:**

bash deployment.sh

2. **Ensure Nginx is properly configured and running.**

---
