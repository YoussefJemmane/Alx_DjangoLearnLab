# RETRIEVE Operation

## Command
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
print(f'Book ID: {book.id}')
print(f'Title: {book.title}')
print(f'Author: {book.author}')
print(f'Publication Year: {book.publication_year}')
```

## Expected Output
```
Book retrieved successfully!
Book ID: 1
Title: 1984
Author: George Orwell
Publication Year: 1949
String representation: 1984
```

## Description
This command retrieves the Book instance with ID 1 from the database and displays all its attributes:
- **ID**: 1 (Primary key)
- **Title**: "1984"
- **Author**: "George Orwell"
- **Publication Year**: 1949

The string representation shows "1984" due to the `__str__` method returning the book's title.
