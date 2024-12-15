# Django LMS Project

This is a Django-based Learning Management System (LMS) designed to manage and track books, users, and reports. It includes Docker deployment for easy containerization.

---

## Installation

### Prerequisites
- Python 3.x
- Docker (if running in containers)
- Docker Compose (for multi-container applications)
- Render account (for deployment)

---

## Steps to Run the Project

### Setting Up the Environment

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application Locally

1. **Set up the PostgreSQL Database:**
   - Install and run PostgreSQL locally or use a cloud database service.
   - Update your database settings in `settings.py`.

2. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

3. **Run the Django Development Server:**
   ```bash
   python manage.py runserver
   ```
   Now, the application should be accessible at [http://localhost:8000/](http://localhost:8000/).

### Setting Up Celery

1. **Install Redis (or any other message broker):**
   - If you're running locally, you can use Redis as the message broker:
     ```bash
     docker-compose up redis
     ```

2. **Start Celery Worker:**
   - Run the following command in a separate terminal window:
     ```bash
     celery -A lmsApp worker --loglevel=info
     ```

3. **Start Celery Beat (if you have periodic tasks):**
   - Run the following command in another terminal window:
     ```bash
     celery -A lmsApp beat --loglevel=info
     ```
   Now, your background tasks should be handled by Celery.

---

## Approach

The project is a Django-based Learning Management System (LMS) that uses several modern tools and techniques:

- **Docker:** Containerization of the Django application for easy deployment.
- **PostgreSQL:** Used as the primary database for storing users, books, and other information.
- **Celery:** Used for background task processing (e.g., sending emails, generating reports).
- **JWT Authentication:** Used for user authentication via JSON Web Tokens.
- **API Design:** Created RESTful APIs using Django REST Framework to manage books, users, and reports.
- **Docker Compose:** Used to set up multi-container applications, including the Django app and PostgreSQL database.
- **Render Deployment:** Deployment using Docker on Render for scalable and easy deployment.

---

## Admin Credentials

- **Username:** admin
- **Password:** admin123

---

## Reports

Go to `/reports` to view reports.

---
here is pictures of my LMS
![Screenshot (118)](https://github.com/user-attachments/assets/839f6d19-8eef-436b-8660-831f21bdfd9e)
![Screenshot (119)](https://github.com/user-attachments/assets/164bf1c6-26ea-457b-8e38-ac092e5561af)
![Screenshot (116)](https://github.com/user-attachments/assets/3b48a266-014d-4736-9dcd-f94ced049680)
![Screenshot (117)](https://github.com/user-attachments/assets/c8db1f45-594e-4d72-b109-83a81e253ca7)

