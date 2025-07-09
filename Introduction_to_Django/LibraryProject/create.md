# CREATE Operation

## Command
```python
from bookshelf.models import Book
book = Book(title='1984', author='George Orwell', publication_year=1949)
book.save()
```

## Expected Output
```
Book created successfully!
Book ID: 1
Title: 1984
Author: George Orwell
Publication Year: 1949
```

## Description
This command creates a new Book instance with the specified attributes:
- **Title**: "1984"
- **Author**: "George Orwell" 
- **Publication Year**: 1949

The book is saved to the database and assigned ID 1, indicating successful creation.
