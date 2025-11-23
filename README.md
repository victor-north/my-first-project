# Django Scheduling Application

A comprehensive Django-based scheduling application for managing events and appointments.

## Features

- Create, read, update, and delete events
- Event fields include: title, description, start time, end time, and location
- User-friendly web interface
- Admin panel for advanced management
- Event validation (ensures end time is after start time)
- Pagination for event listings

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Create a superuser (for admin access):
```bash
python manage.py createsuperuser
```

4. Start the development server:
```bash
python manage.py runserver
```

5. Access the application:
   - Main app: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage

### Creating Events
1. Navigate to the home page
2. Click "Create Event" in the navigation
3. Fill in the event details
4. Click "Save Event"

### Viewing Events
- All events are displayed on the home page in chronological order
- Click "View" on any event to see its details

### Editing Events
1. Click "Edit" on any event
2. Modify the desired fields
3. Click "Save Event"

### Deleting Events
1. Click "Delete" on any event
2. Confirm the deletion

### Admin Panel
Access the admin panel at /admin/ to:
- Manage events with advanced filters
- Search events by title, description, or location
- Use date hierarchy for easier navigation

## Project Structure

```
.
├── manage.py
├── requirements.txt
├── scheduling_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── scheduler/
    ├── models.py          # Event model definition
    ├── views.py           # CRUD views
    ├── urls.py            # URL routing
    ├── admin.py           # Admin configuration
    └── templates/
        └── scheduler/     # HTML templates
```

## Technologies Used

- Django 5.2.8
- SQLite (default database)
- Python 3.11+
