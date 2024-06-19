#!/bin/bash
# Deployment script for chatbot application

# Update system packages
sudo apt-get update -y
sudo apt-get upgrade -y

# Install required packages
sudo apt-get install -y python3-pip python3-dev libpq-dev nginx curl

# Install and configure virtual environment
sudo pip3 install virtualenv
virtualenv venv
source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn service
sudo systemctl start gunicorn
sudo systemctl enable gunicorn

# Restart Nginx service
sudo systemctl restart nginx

echo "Deployment complete!"
