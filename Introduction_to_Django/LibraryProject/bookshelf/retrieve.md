# RETRIEVE Operation

## Objective
Retrieve and display all attributes of the book that was just created.

## Django Shell Commands
```python
from bookshelf.models import Book

# Retrieve the book with ID 7 (the one we just created)
book = Book.objects.get(id=7)

# Display all book details
print('Book retrieved successfully!')
print(f'ID: {book.id}')
print(f'Title: {book.title}')
print(f'Author: {book.author}')
print(f'Publication Year: {book.publication_year}')
print(f'String representation: {str(book)}')

# Also show all attributes using vars()
print('\nAll attributes:')
for key, value in vars(book).items():
    if not key.startswith('_'):
        print(f'{key}: {value}')
```

## Expected Output
```
Book retrieved successfully!
ID: 7
Title: 1984
Author: George Orwell
Publication Year: 1949
String representation: 1984

All attributes:
id: 7
title: 1984
author: George Orwell
publication_year: 1949
```

## Explanation
1. **Import Model**: Import the Book model from bookshelf.models
2. **Retrieve Object**: Use `Book.objects.get(id=7)` to fetch the specific book
3. **Display Attributes**: Access and display each attribute individually
4. **String Representation**: Show the `__str__` method output
5. **All Attributes**: Use `vars()` to display all object attributes

## Result
- Successfully retrieved the Book instance with ID 7
- All attributes are correctly displayed:
  - **ID**: 7 (Primary key)
  - **Title**: "1984"
  - **Author**: "George Orwell"
  - **Publication Year**: 1949
- The string representation shows "1984" due to the `__str__` method
