# LibraryProject - Django Book Management System

## Overview
LibraryProject is a Django-based web application for managing books in a library system. It demonstrates fundamental Django concepts including models, admin interface, and CRUD operations.

## Features
- **Book Model**: Manage books with title, author, and publication year
- **Django Admin Interface**: Full admin capabilities with custom configurations
- **CRUD Operations**: Complete Create, Read, Update, Delete functionality
- **Search & Filter**: Advanced search and filtering in admin interface
- **Database Integration**: SQLite database with Django ORM

## Project Structure
```
LibraryProject/
├── LibraryProject/          # Main project directory
│   ├── __init__.py
│   ├── settings.py         # Django settings
│   ├── urls.py            # URL configuration
│   └── wsgi.py            # WSGI configuration
├── bookshelf/              # Main app directory
│   ├── __init__.py
│   ├── admin.py           # Admin interface configuration
│   ├── apps.py            # App configuration
│   ├── models.py          # Book model definition
│   ├── views.py           # View functions
│   ├── tests.py           # Test cases
│   ├── create.md          # CREATE operation documentation
│   ├── retrieve.md        # RETRIEVE operation documentation
│   ├── update.md          # UPDATE operation documentation
│   ├── delete.md          # DELETE operation documentation
│   └── migrations/        # Database migrations
├── manage.py              # Django management script
├── db.sqlite3             # SQLite database
├── CRUD_operations.md     # Comprehensive CRUD documentation
├── django_admin_setup.md  # Admin interface setup guide
├── admin_quick_reference.md # Admin quick reference
└── README.md              # This file
```

## Models

### Book Model
```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
```

## Admin Interface Features
- **List Display**: Shows title, author, and publication year
- **Search Functionality**: Search by title and author
- **Filters**: Filter by author and publication year
- **Ordering**: Alphabetical ordering by title
- **Full CRUD**: Add, edit, delete books through admin interface

## Installation & Setup

### Prerequisites
- Python 3.x
- Django 4.2.11
- Ubuntu/Linux environment

### Installation Steps
1. **Install Django**:
   ```bash
   sudo apt update
   sudo apt install python3-django
   ```

2. **Navigate to project directory**:
   ```bash
   cd /path/to/LibraryProject
   ```

3. **Run migrations**:
   ```bash
   python3 manage.py migrate
   ```

4. **Create superuser** (for admin access):
   ```bash
   python3 manage.py createsuperuser
   ```

5. **Start development server**:
   ```bash
   python3 manage.py runserver
   ```

6. **Access the application**:
   - Main site: `http://localhost:8000/`
   - Admin interface: `http://localhost:8000/admin/`

## Usage

### Django Shell Operations
The project includes comprehensive CRUD operations documentation:

- **Create**: `bookshelf/create.md`
- **Retrieve**: `bookshelf/retrieve.md`
- **Update**: `bookshelf/update.md`
- **Delete**: `bookshelf/delete.md`

### Admin Interface
1. Start the server: `python3 manage.py runserver`
2. Navigate to: `http://localhost:8000/admin/`
3. Login with superuser credentials
4. Manage books through the intuitive admin interface

## Sample Data
The project includes sample books for testing:
- To Kill a Mockingbird (Harper Lee, 1960)
- 1984 (George Orwell, 1949)
- Pride and Prejudice (Jane Austen, 1813)
- The Great Gatsby (F. Scott Fitzgerald, 1925)
- Animal Farm (George Orwell, 1945)

## Documentation

### CRUD Operations
- **`CRUD_operations.md`**: Comprehensive guide to all CRUD operations
- **`bookshelf/create.md`**: Detailed CREATE operation documentation
- **`bookshelf/retrieve.md`**: Detailed RETRIEVE operation documentation
- **`bookshelf/update.md`**: Detailed UPDATE operation documentation
- **`bookshelf/delete.md`**: Detailed DELETE operation documentation

### Admin Interface
- **`django_admin_setup.md`**: Complete admin interface setup guide
- **`admin_quick_reference.md`**: Quick reference for admin operations

## Key Django Concepts Demonstrated

1. **Models**: Django ORM with Book model
2. **Admin Interface**: Customized admin with search, filters, and ordering
3. **Database Operations**: Full CRUD operations via Django shell
4. **Migrations**: Database schema management
5. **Settings Configuration**: App registration and database setup
6. **Project Structure**: Standard Django project organization

## Testing

### Manual Testing
1. **Admin Interface Testing**:
   - Test all CRUD operations through admin
   - Verify search and filter functionality
   - Check ordering and pagination

2. **Django Shell Testing**:
   - Execute commands from CRUD documentation files
   - Verify database operations
   - Test model methods and relationships

### Test Commands
```bash
# Run Django shell
python3 manage.py shell

# Test database connection
python3 manage.py dbshell

# Check for issues
python3 manage.py check
```

## Technologies Used
- **Django 4.2.11**: Web framework
- **Python 3.x**: Programming language
- **SQLite**: Database
- **Django ORM**: Object-Relational Mapping
- **Django Admin**: Built-in administration interface

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License
This project is for educational purposes as part of the ALX Django Learning Lab.

## Support
For questions or issues, please refer to the comprehensive documentation files included in the project.

---

**Author**: ALX Django Learning Lab  
**Last Updated**: July 2025  
**Django Version**: 4.2.11
