# Django REST Framework API Project

This project implements a complete API using Django REST Framework with authentication, permissions, and full CRUD operations for managing books.

## Features

- **Django REST Framework integration**
- **Token-based authentication**
- **Permission-based access control**
- **Full CRUD operations via ViewSets**
- **API endpoints for book management**

## Setup

1. **Virtual Environment** (already created):
   ```bash
   source ../api_env/bin/activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install django djangorestframework
   ```

3. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

5. **Start Development Server**:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- **POST** `/api/auth/token/` - Obtain authentication token
  - Body: `{"username": "your_username", "password": "your_password"}`

### Book Management

#### Simple List View
- **GET** `/api/books/` - List all books (requires authentication)

#### Full CRUD Operations (ViewSet)
- **GET** `/api/books_all/` - List all books
- **POST** `/api/books_all/` - Create a new book
- **GET** `/api/books_all/{id}/` - Retrieve a specific book
- **PUT** `/api/books_all/{id}/` - Update a book
- **PATCH** `/api/books_all/{id}/` - Partially update a book
- **DELETE** `/api/books_all/{id}/` - Delete a book

## Authentication

All API endpoints require authentication using Token Authentication. Include the token in your request headers:

```
Authorization: Token your_token_here
```

## Example Usage

### 1. Get Authentication Token
```bash
curl -X POST http://127.0.0.1:8000/api/auth/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "admin", "password": "admin123"}'
```

### 2. Create a Book
```bash
curl -X POST http://127.0.0.1:8000/api/books_all/ \
     -H "Authorization: Token your_token_here" \
     -H "Content-Type: application/json" \
     -d '{"title": "Django REST Framework Guide", "author": "John Doe"}'
```

### 3. List All Books
```bash
curl -X GET http://127.0.0.1:8000/api/books_all/ \
     -H "Authorization: Token your_token_here"
```

### 4. Update a Book
```bash
curl -X PUT http://127.0.0.1:8000/api/books_all/1/ \
     -H "Authorization: Token your_token_here" \
     -H "Content-Type: application/json" \
     -d '{"title": "Updated Title", "author": "Updated Author"}'
```

### 5. Delete a Book
```bash
curl -X DELETE http://127.0.0.1:8000/api/books_all/1/ \
     -H "Authorization: Token your_token_here"
```

## Models

### Book Model
- `id` (AutoField) - Primary key
- `title` (CharField) - Book title (max 200 characters)
- `author` (CharField) - Book author (max 100 characters)
- `created_at` (DateTimeField) - Creation timestamp
- `updated_at` (DateTimeField) - Last update timestamp

## Permissions

- All endpoints require authentication
- Uses `IsAuthenticated` permission class
- Token-based authentication is configured globally

## Project Structure

```
api_project/
├── api_project/
│   ├── __init__.py
│   ├── settings.py      # Django settings with DRF configuration
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py
├── api/
│   ├── __init__.py
│   ├── models.py        # Book model
│   ├── serializers.py   # Book serializer
│   ├── views.py         # API views (ListAPIView & ViewSet)
│   ├── urls.py          # API URL patterns
│   └── migrations/
├── manage.py
└── README.md
```

## Testing

You can test the API using:
- **curl** (command line)
- **Postman** (GUI application)
- **Django REST Framework Browsable API** (built-in web interface)
- **httpie** (command line HTTP client)

Visit http://127.0.0.1:8000/api/ to access the browsable API interface.
