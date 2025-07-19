# Django Models Project - Advanced Relationships

This Django project demonstrates advanced model relationships, views, authentication, role-based access control, and custom permissions.

## Project Structure

```
django-models/
└── LibraryProject/
    ├── LibraryProject/
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    ├── relationship_app/
    │   ├── models.py          # Complex model relationships
    │   ├── views.py           # Function-based and class-based views
    │   ├── urls.py            # URL configurations
    │   ├── admin.py           # Admin interface setup
    │   ├── query_samples.py   # Sample ORM queries
    │   └── templates/
    │       └── relationship_app/
    │           ├── list_books.html
    │           ├── library_detail.html
    │           ├── login.html
    │           ├── logout.html
    │           ├── register.html
    │           ├── admin_view.html
    │           ├── librarian_view.html
    │           ├── member_view.html
    │           ├── add_book.html
    │           ├── edit_book.html
    │           └── delete_book.html
    └── manage.py
```

## Features Implemented

### 1. Advanced Model Relationships

**Models defined in `models.py`:**

- **Author**: Basic model with name field
- **Book**: ForeignKey relationship to Author, with custom permissions
- **Library**: ManyToManyField relationship to Book
- **Librarian**: OneToOneField relationship to Library
- **UserProfile**: Extends User model with role-based access control

**Custom Permissions on Book model:**
- `can_add_book`: Permission to add new books
- `can_change_book`: Permission to modify existing books  
- `can_delete_book`: Permission to delete books

### 2. Django Views and URL Configuration

**Function-based View:**
- `list_books()`: Displays all books with authors

**Class-based View:**
- `LibraryDetailView`: Shows library details and associated books

**URL Patterns:**
- `/relationship/books/` - List all books
- `/relationship/library/<id>/` - Library detail view

### 3. User Authentication

**Authentication Views:**
- `CustomLoginView`: User login functionality
- `CustomLogoutView`: User logout functionality  
- `register_view()`: User registration

**Authentication URLs:**
- `/relationship/login/` - User login
- `/relationship/logout/` - User logout
- `/relationship/register/` - User registration

### 4. Role-Based Access Control

**User Roles:**
- **Admin**: Full system access
- **Librarian**: Library management access
- **Member**: Basic user access

**Role-based Views:**
- `admin_view()`: Admin dashboard (requires Admin role)
- `librarian_view()`: Librarian dashboard (requires Librarian role)
- `member_view()`: Member portal (requires Member role)

**Role-based URLs:**
- `/relationship/admin-view/` - Admin dashboard
- `/relationship/librarian-view/` - Librarian dashboard  
- `/relationship/member-view/` - Member portal

### 5. Custom Permissions Implementation

**Permission-secured Views:**
- `add_book_view()`: Requires `can_add_book` permission
- `edit_book_view()`: Requires `can_change_book` permission
- `delete_book_view()`: Requires `can_delete_book` permission

**Permission URLs:**
- `/relationship/add_book/` - Add new book
- `/relationship/edit_book/<id>/` - Edit existing book
- `/relationship/delete_book/<id>/` - Delete book

## Sample Queries

The `query_samples.py` file demonstrates ORM relationships:

1. **Query books by author**: `Book.objects.filter(author=author)`
2. **List books in library**: `library.books.all()`
3. **Get librarian for library**: `Librarian.objects.get(library=library)`

## Setup Instructions

1. **Install Dependencies:**
   ```bash
   pip install django
   ```

2. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create Superuser:**
   ```bash
   python manage.py createsuperuser
   ```

4. **Run Development Server:**
   ```bash
   python manage.py runserver
   ```

5. **Test Sample Queries:**
   ```bash
   python relationship_app/query_samples.py
   ```

## Key Learning Objectives

- **Model Relationships**: ForeignKey, ManyToManyField, OneToOneField
- **Django Views**: Function-based vs Class-based views
- **Authentication**: Login, logout, registration
- **Authorization**: Role-based access control
- **Permissions**: Custom model permissions
- **Django ORM**: Complex queries and relationships
- **Template System**: HTML templates with Django template language

## Usage Examples

### Accessing Role-based Views
Users must be logged in and have appropriate roles to access:
- Admins can access `/relationship/admin-view/`
- Librarians can access `/relationship/librarian-view/`
- Members can access `/relationship/member-view/`

### Managing Books with Permissions
Users need specific permissions to:
- Add books: Navigate to `/relationship/add_book/`
- Edit books: Navigate to `/relationship/edit_book/<book_id>/`
- Delete books: Navigate to `/relationship/delete_book/<book_id>/`

### Viewing Data
- View all books: `/relationship/books/`
- View library details: `/relationship/library/<library_id>/`

This project serves as a comprehensive example of Django's ORM capabilities, authentication system, and permission framework.
