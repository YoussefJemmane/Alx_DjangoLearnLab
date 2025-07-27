# DELETE Operation

## Objective
Delete the book created and confirm the deletion by trying to retrieve all books again.

## Django Shell Commands

### Method 1: Using Book.objects.get() + delete() for single object
```python
from bookshelf.models import Book

# Show all books before deletion
print('Before deletion:')
all_books = Book.objects.all()
print(f'Total number of books: {all_books.count()}')
for book in all_books:
    print(f'ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.publication_year}')

# Find and delete the specific book
book_to_delete = Book.objects.get(id=8)
print(f'\nDeleting book: {book_to_delete.title} by {book_to_delete.author}')
book_to_delete.delete()

# Show all books after deletion
print('\nAfter deletion:')
all_books = Book.objects.all()
print(f'Total number of books: {all_books.count()}')
for book in all_books:
    print(f'ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.publication_year}')

# Try to retrieve the deleted book to confirm deletion
try:
    deleted_book = Book.objects.get(id=8)
    print(f'Book still exists: {deleted_book.title}')
except Book.DoesNotExist:
    print('\nConfirmation: Book with ID 8 no longer exists in the database')

print('\nDeletion completed successfully!')
```

### Method 2: Using Book.objects.filter().delete() for bulk deletion
```python
from bookshelf.models import Book

# Show books before bulk deletion
books_to_delete = Book.objects.filter(author='George Orwell')
print('Before bulk deletion:')
print(f'Books by George Orwell ({books_to_delete.count()} found):')
for book in books_to_delete:
    print(f'ID: {book.id}, Title: {book.title}, Year: {book.publication_year}')

# Bulk delete all books by George Orwell
deleted_count, deleted_details = Book.objects.filter(author='George Orwell').delete()
print(f'\nBulk deletion completed!')
print(f'Deleted {deleted_count} objects: {deleted_details}')

# Show remaining books
remaining_books = Book.objects.all()
print(f'\nRemaining books ({remaining_books.count()}):')
for book in remaining_books:
    print(f'ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.publication_year}')
```

### Method 3: Using Book.objects.all().delete() for complete deletion
```python
from bookshelf.models import Book

# Show all books before complete deletion
all_books = Book.objects.all()
print(f'Before complete deletion: {all_books.count()} books')
for book in all_books:
    print(f'ID: {book.id}, Title: {book.title}, Author: {book.author}')

# Delete all books
deleted_count, deleted_details = Book.objects.all().delete()
print(f'\nAll books deleted!')
print(f'Deleted {deleted_count} objects: {deleted_details}')

# Confirm no books remain
remaining_books = Book.objects.all()
print(f'\nRemaining books: {remaining_books.count()}')
if remaining_books.count() == 0:
    print('Database is now empty!')
```

### Method 4: Safe deletion with Book.objects.filter().exists()
```python
from bookshelf.models import Book

# Check if book exists before attempting deletion
book_id = 8
if Book.objects.filter(id=book_id).exists():
    book = Book.objects.get(id=book_id)
    print(f'Found book: {book.title} by {book.author}')
    book.delete()
    print('Book deleted successfully!')
else:
    print(f'Book with ID {book_id} does not exist')

# Verify deletion
if not Book.objects.filter(id=book_id).exists():
    print(f'Confirmed: Book with ID {book_id} no longer exists')
```

## Expected Output

### Method 1 Output (objects.get + delete)
```
Before deletion:
Total number of books: 7
ID: 2, Title: To Kill a Mockingbird, Author: Harper Lee, Year: 1960
ID: 3, Title: 1984, Author: George Orwell, Year: 1949
ID: 4, Title: Pride and Prejudice, Author: Jane Austen, Year: 1813
ID: 5, Title: The Great Gatsby, Author: F. Scott Fitzgerald, Year: 1925
ID: 6, Title: Animal Farm, Author: George Orwell, Year: 1945
ID: 8, Title: Nineteen Eighty-Four, Author: George Orwell, Year: 1949
ID: 9, Title: The Hobbit, Author: J.R.R. Tolkien, Year: 1937

Deleting book: Nineteen Eighty-Four by George Orwell

After deletion:
Total number of books: 6
ID: 2, Title: To Kill a Mockingbird, Author: Harper Lee, Year: 1960
ID: 3, Title: 1984, Author: George Orwell, Year: 1949
ID: 4, Title: Pride and Prejudice, Author: Jane Austen, Year: 1813
ID: 5, Title: The Great Gatsby, Author: F. Scott Fitzgerald, Year: 1925
ID: 6, Title: Animal Farm, Author: George Orwell, Year: 1945
ID: 9, Title: The Hobbit, Author: J.R.R. Tolkien, Year: 1937

Confirmation: Book with ID 8 no longer exists in the database

Deletion completed successfully!
```

### Method 2 Output (objects.filter.delete)
```
Before bulk deletion:
Books by George Orwell (2 found):
ID: 3, Title: 1984, Year: 1949
ID: 6, Title: Animal Farm, Year: 1945

Bulk deletion completed!
Deleted 2 objects: {'bookshelf.Book': 2}

Remaining books (4):
ID: 2, Title: To Kill a Mockingbird, Author: Harper Lee, Year: 1960
ID: 4, Title: Pride and Prejudice, Author: Jane Austen, Year: 1813
ID: 5, Title: The Great Gatsby, Author: F. Scott Fitzgerald, Year: 1925
ID: 9, Title: The Hobbit, Author: J.R.R. Tolkien, Year: 1937
```

### Method 3 Output (objects.all.delete)
```
Before complete deletion: 4 books
ID: 2, Title: To Kill a Mockingbird, Author: Harper Lee
ID: 4, Title: Pride and Prejudice, Author: Jane Austen
ID: 5, Title: The Great Gatsby, Author: F. Scott Fitzgerald
ID: 9, Title: The Hobbit, Author: J.R.R. Tolkien

All books deleted!
Deleted 4 objects: {'bookshelf.Book': 4}

Remaining books: 0
Database is now empty!
```

### Method 4 Output (safe deletion with exists)
```
Book with ID 8 does not exist
Confirmed: Book with ID 8 no longer exists
```

## Explanation

### Method 1: Book.objects.get() + delete()
- **Purpose**: Delete a single object with confirmation
- **Process**: Retrieve → Delete → Verify
- **Use Case**: When you need to delete a specific object
- **Safety**: Raises exception if object doesn't exist
- **Returns**: Tuple (deleted_count, {model: count})

### Method 2: Book.objects.filter().delete()
- **Purpose**: Bulk delete multiple objects efficiently
- **Process**: Filter → Delete in database directly
- **Use Case**: When deleting multiple objects with same criteria
- **Performance**: Single SQL DELETE query
- **Returns**: Tuple (deleted_count, {model: count})

### Method 3: Book.objects.all().delete()
- **Purpose**: Delete all objects from the table
- **Process**: Select all → Delete all
- **Use Case**: When clearing entire table (use with caution!)
- **Performance**: Single SQL DELETE query
- **Warning**: Irreversible operation - use carefully

### Method 4: Book.objects.filter().exists() + delete()
- **Purpose**: Safe deletion with existence check
- **Process**: Check existence → Delete if exists
- **Use Case**: When you want to avoid exceptions
- **Safety**: Prevents errors if object doesn't exist
- **Best Practice**: Recommended for production code

## Objects Manager Delete Methods Summary

| Method | Purpose | Performance | Safety | Use Case |
|--------|---------|-------------|--------|----------|
| `get() + delete()` | Single object | Standard | Exception on missing | Specific deletion |
| `filter().delete()` | Bulk deletion | High performance | Silent if none found | Conditional deletion |
| `all().delete()` | Complete deletion | High performance | Dangerous | Clear all data |
| `exists() + delete()` | Safe deletion | Standard + check | No exceptions | Production safe |

## Important Notes

- **Cascade Behavior**: Deletions respect foreign key constraints and CASCADE settings
- **Signals**: Individual `delete()` calls trigger Django signals, bulk `delete()` does not
- **Transactions**: All deletions are wrapped in database transactions
- **Irreversible**: Deletions are permanent unless within a transaction that's rolled back

## Result
- Successfully demonstrated multiple deletion methods using Django's objects manager
- Each method serves different safety and performance requirements
- Bulk deletions are more efficient for large datasets
- Safe deletion methods prevent exceptions and errors
- All methods return deletion counts for confirmation
- Django ORM handles SQL generation and constraint enforcement
