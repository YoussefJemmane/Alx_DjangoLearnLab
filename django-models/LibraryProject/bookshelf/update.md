# UPDATE Operation

## Objective
Update the title of "1984" to "Nineteen Eighty-Four" and save the changes.

## Django Shell Commands

### Method 1: Using Book.objects.get() + save() for single object
```python
from bookshelf.models import Book

# Retrieve the book with ID 8
book = Book.objects.get(id=8)

# Show current state
print('Before update:')
print(f'ID: {book.id}')
print(f'Title: {book.title}')
print(f'Author: {book.author}')
print(f'Publication Year: {book.publication_year}')

# Update the title
book.title = 'Nineteen Eighty-Four'
book.save()

# Show updated state
print('\nAfter update:')
print(f'ID: {book.id}')
print(f'Title: {book.title}')
print(f'Author: {book.author}')
print(f'Publication Year: {book.publication_year}')
print(f'String representation: {str(book)}')

print('\nUpdate completed successfully!')
```

### Method 2: Using Book.objects.filter().update() for bulk updates
```python
from bookshelf.models import Book
from django.db import models

# Show books before update
books_1949 = Book.objects.filter(publication_year=1949)
print('Before bulk update:')
for book in books_1949:
    print(f'ID: {book.id}, Title: {book.title}, Author: {book.author}')

# Bulk update all books from 1949 - add " (Classic)" to titles
updated_count = Book.objects.filter(publication_year=1949).update(
    title=models.F('title') + ' (Classic)'
)

print(f'\n{updated_count} books updated!')

# Show books after update
books_1949_updated = Book.objects.filter(publication_year=1949)
print('\nAfter bulk update:')
for book in books_1949_updated:
    print(f'ID: {book.id}, Title: {book.title}, Author: {book.author}')
```

### Method 3: Using Book.objects.get_or_create() for conditional update
```python
from bookshelf.models import Book

# Try to get or create a book
book, created = Book.objects.get_or_create(
    title='The Hobbit',
    author='J.R.R. Tolkien',
    defaults={'publication_year': 1937}
)

if created:
    print(f'Created new book: {book.title} by {book.author}')
else:
    print(f'Book already exists: {book.title} by {book.author}')
    # Update existing book
    book.publication_year = 1937
    book.save()
    print('Updated publication year')

print(f'Final: ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.publication_year}')
```

### Method 4: Using Book.objects.update_or_create() for advanced updates
```python
from bookshelf.models import Book

# Update or create based on title and author
book, created = Book.objects.update_or_create(
    title='Animal Farm',
    author='George Orwell',
    defaults={'publication_year': 1945}
)

if created:
    print(f'Created: {book.title} by {book.author} ({book.publication_year})')
else:
    print(f'Updated: {book.title} by {book.author} ({book.publication_year})')

print(f'Result: ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.publication_year}')
```

## Expected Output

### Method 1 Output (objects.get + save)
```
Before update:
ID: 8
Title: 1984
Author: George Orwell
Publication Year: 1949

After update:
ID: 8
Title: Nineteen Eighty-Four
Author: George Orwell
Publication Year: 1949
String representation: Nineteen Eighty-Four

Update completed successfully!
```

### Method 2 Output (objects.filter.update)
```
Before bulk update:
ID: 3, Title: 1984, Author: George Orwell
ID: 8, Title: Nineteen Eighty-Four, Author: George Orwell

2 books updated!

After bulk update:
ID: 3, Title: 1984 (Classic), Author: George Orwell
ID: 8, Title: Nineteen Eighty-Four (Classic), Author: George Orwell
```

### Method 3 Output (objects.get_or_create)
```
Created new book: The Hobbit by J.R.R. Tolkien
Final: ID: 9, Title: The Hobbit, Author: J.R.R. Tolkien, Year: 1937
```

### Method 4 Output (objects.update_or_create)
```
Updated: Animal Farm by George Orwell (1945)
Result: ID: 6, Title: Animal Farm, Author: George Orwell, Year: 1945
```

## Explanation

### Method 1: Book.objects.get() + save()
- **Purpose**: Update a single object with precise control
- **Process**: Retrieve → Modify → Save
- **Use Case**: When you need to update specific fields with validation
- **Performance**: Single object update, triggers model validation and signals

### Method 2: Book.objects.filter().update()
- **Purpose**: Bulk update multiple objects efficiently
- **Process**: Filter → Update in database directly
- **Use Case**: When updating many objects with the same change
- **Performance**: Single SQL UPDATE query, bypasses model validation
- **Note**: Uses F() expressions for database-level operations

### Method 3: Book.objects.get_or_create()
- **Purpose**: Get existing object or create new one
- **Returns**: Tuple (object, created_boolean)
- **Use Case**: When you want to ensure an object exists
- **Safety**: Prevents duplicate creation, handles race conditions

### Method 4: Book.objects.update_or_create()
- **Purpose**: Update existing object or create new one
- **Returns**: Tuple (object, created_boolean)
- **Use Case**: When you want to upsert (update or insert)
- **Flexibility**: Combines update and create logic

## Objects Manager Update Methods Summary

| Method | Purpose | Performance | Use Case | Validation |
|--------|---------|-------------|----------|------------|
| `get() + save()` | Single object update | Standard | Precise control | Full validation |
| `filter().update()` | Bulk update | High performance | Mass updates | No validation |
| `get_or_create()` | Get or create | Standard | Ensure existence | Create validation |
| `update_or_create()` | Update or create | Standard | Upsert operations | Create/Update validation |

## Result
- Successfully demonstrated multiple update methods using Django's objects manager
- Each method serves different performance and use case requirements
- Bulk updates are more efficient for large datasets
- Individual updates provide better control and validation
- Django ORM handles SQL generation and database abstraction
