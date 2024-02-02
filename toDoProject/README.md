# Django ToDo App

## Overview

Welcome to the Django ToDo App project! This application allows you to manage your tasks through a simple ToDo list with CRUD (Create, Read, Update, Delete) operations.

## Features

- View a list of ToDo items
- See detailed information about a specific ToDo item
- Add a new ToDo item
- Edit an existing ToDo item
- Delete a ToDo item

## Project Structure

The project structure includes the following components:

- **todo_app:** Django app containing the models, views, forms, and templates for the ToDo app.
- **templates:** Folder containing HTML templates for rendering views.
- **static:** Folder for storing static files such as CSS, JavaScript, and images.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/alby-tomy/Django_Beginner_level.git
   cd Django_Beginner_level
  
2. **Activate Virtual Environment:**
   ```bash
   cd DjangoSt
   source bin/activate
3. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
4. **Create Superuser(Optional):**
   ```bash
   python manage.py createsuperuser
5. **Run the Development Server:**
   ```bash
   python manage.py runserver
  ### The application will be accessible at http://127.0.0.1:8000/ in your web browser.
6. **Access the Admin Panel**
- Navigate to http://127.0.0.1:8000/admin/ and log in with the superuser credentials (if created).



# **Usage**
## View ToDo List:

- Open http://127.0.0.1:8000/ in your web browser to view the list of ToDo items.

## Manage ToDo Items:
- Click on each ToDo item to view details, edit, or delete it.
- Use the "Add ToDo" button to create a new ToDo item.

## Admin Panel:
- Access the Django admin panel at http://127.0.0.1:8000/admin/ for more advanced management (requires superuser credentials).

## Customization
- Feel free to customize and expand the ToDo app based on your specific requirements. You can add more features, improve the user interface, or integrate additional functionalities.

## Interface
![Alt Text](Django_Beginner_level/toDoProject/interface/Screenshot from 2024-02-02 05-28-43.png)

   

