from celery import shared_task
import json
from datetime import datetime
from django.conf import settings
from .models import Author, Book, Borrow
import os

# lmsApp/tasks.py



@shared_task
def generate_report():
    # Get the total number of authors
    total_authors = Author.objects.count()

    # Get the total number of books
    total_books = Book.objects.count()

    # Get the total number of currently borrowed books
    borrowed_books = Borrow.objects.filter(return_date__isnull=True).count()

    # Prepare the report data
    report_data = {
        'total_authors': total_authors,
        'total_books': total_books,
        'borrowed_books': borrowed_books,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    # Create a directory to store the reports if it doesn't exist
    reports_dir = os.path.join(settings.BASE_DIR, 'reports')
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    # Create a timestamped report file
    timestamp = datetime.now().strftime('%Y%m%d')
    report_filename = f"report_{timestamp}.json"
    report_filepath = os.path.join(reports_dir, report_filename)

    # Save the report to the file
    with open(report_filepath, 'w') as report_file:
        json.dump(report_data, report_file, indent=4)

    return report_filepath
