Django LMS Project
This is a Django-based Learning Management System (LMS) designed to manage and track books, users, and reports. It includes Docker deployment for easy containerization 
Installation
Prerequisites
Python 3.x
Docker (if running in containers)
Docker Compose (for multi-container applications)
Vercel account (for deployment)
Steps to Run the Project
Setting Up the Environment
Clone the repository:
Install required dependencies:
pip install -r requirements.txt

Running the Application Locally
Set up the PostgreSQL Database:

You need to install and run PostgreSQL locally or use a cloud database service.
Update your database settings in settings.py.
Apply Migrations:

bash
Copy code
python manage.py migrate
Run the Django Development Server:

bash
Copy code
python manage.py runserver
Now, the application should be accessible at http://localhost:8000/.

Setting Up Celery
Install Redis (or any other message broker):

If you're running locally, you can use Redis as the message broker:

bash
Copy code
docker-compose up redis
Start Celery Worker:

Run the following command in a separate terminal window:

bash
Copy code
celery -A lmsApp worker --loglevel=info
Start Celery Beat (if you have periodic tasks):

bash
Copy code
celery -A lmsApp beat --loglevel=info
Now, your background tasks should be handled by Celery.

Approach
The project is a Django-based Learning Management System (LMS) that uses several modern tools and techniques:

Docker: Containerization of the Django application for easy deployment.
PostgreSQL: Used as the primary database for storing users, books, and other information.
Celery: Used for background task processing (e.g., sending emails, generating reports).
JWT Authentication: Used for user authentication via JSON Web Tokens.
API Design: Created RESTful APIs using Django REST Framework to manage books, users, and reports.
Docker Compose: Used to set up multi-container applications, including the Django app and PostgreSQL database.
Vercel Deployment: Deployment using Docker on Vercel for scalable and easy deployment.

Admin Credentials
Username: admin
Password: admin123

go to /reports to see Reports
