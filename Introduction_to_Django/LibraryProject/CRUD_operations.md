# CRUD Operations Documentation

This document contains all the CRUD (Create, Read, Update, Delete) operations performed on the Book model in the Django shell.

## Book Model Definition

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
```

## 1. CREATE Operation

### Command:
```python
from bookshelf.models import Book
book = Book(title='1984', author='George Orwell', publication_year=1949)
book.save()
```

### Output:
```
Book created successfully!
Book ID: 1
Title: 1984
Author: George Orwell
Publication Year: 1949
```

### Description:
Created a new Book instance with title "1984", author "George Orwell", and publication year 1949. The book was assigned ID 1 upon successful creation.

---

## 2. RETRIEVE Operation

### Command:
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
print(f'Book ID: {book.id}')
print(f'Title: {book.title}')
print(f'Author: {book.author}')
print(f'Publication Year: {book.publication_year}')
```

### Output:
```
Book retrieved successfully!
Book ID: 1
Title: 1984
Author: George Orwell
Publication Year: 1949
String representation: 1984
```

### Description:
Successfully retrieved the Book instance with ID 1 and displayed all its attributes. The string representation shows "1984" due to the `__str__` method.

---

## 3. UPDATE Operation

### Command:
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.title = 'Nineteen Eighty-Four'
book.save()
```

### Output:
```
Before update:
Title: 1984
After update:
Title: Nineteen Eighty-Four
Book updated successfully!
```

### Description:
Updated the title of the book from "1984" to "Nineteen Eighty-Four". The change was saved to the database and confirmed by displaying the title before and after the update.

---

## 4. DELETE Operation

### Command:
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.delete()

# Confirm deletion
books = Book.objects.all()
print(f'Number of books: {books.count()}')
```

### Output:
```
Before deletion:
Number of books: 1
Book: Nineteen Eighty-Four by George Orwell
Book deleted successfully!
After deletion:
Number of books: 0
No books found in database
```

### Description:
Deleted the Book instance with ID 1 from the database. The deletion was confirmed by querying all books, showing that the count reduced from 1 to 0.

---

## Summary

All CRUD operations were successfully performed on the Book model:

1. **CREATE**: Created a book "1984" by George Orwell (1949)
2. **RETRIEVE**: Retrieved and displayed the book's details
3. **UPDATE**: Changed the title to "Nineteen Eighty-Four"
4. **DELETE**: Removed the book from the database

The operations demonstrate full database interaction capabilities using Django ORM.
