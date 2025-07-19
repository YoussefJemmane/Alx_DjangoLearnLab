# RETRIEVE Operation

## Objective
Retrieve and display all attributes of the book that was just created.

## Django Shell Commands

### Method 1: Using Book.objects.get() for single object
```python
from bookshelf.models import Book

# Retrieve a specific book by ID
book = Book.objects.get(id=8)

# Display all book details
print('Book retrieved successfully using objects.get()!')
print(f'ID: {book.id}')
print(f'Title: {book.title}')
print(f'Author: {book.author}')
print(f'Publication Year: {book.publication_year}')
print(f'String representation: {str(book)}')
```

### Method 2: Using Book.objects.all() for all objects
```python
from bookshelf.models import Book

# Retrieve all books
all_books = Book.objects.all()

print(f'Retrieved {all_books.count()} books:')
for book in all_books:
    print(f'ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.publication_year}')
```

### Method 3: Using Book.objects.filter() for filtered results
```python
from bookshelf.models import Book

# Filter books by author
orwell_books = Book.objects.filter(author='George Orwell')

print(f'Books by George Orwell ({orwell_books.count()} found):')
for book in orwell_books:
    print(f'ID: {book.id}, Title: {book.title}, Year: {book.publication_year}')

# Filter books by publication year
books_1949 = Book.objects.filter(publication_year=1949)

print(f'\nBooks published in 1949 ({books_1949.count()} found):')
for book in books_1949:
    print(f'ID: {book.id}, Title: {book.title}, Author: {book.author}')
```

### Method 4: Using Book.objects.first() and Book.objects.last()
```python
from bookshelf.models import Book

# Get first book (by ID order)
first_book = Book.objects.first()
if first_book:
    print(f'First book: {first_book.title} by {first_book.author}')

# Get last book (by ID order)
last_book = Book.objects.last()
if last_book:
    print(f'Last book: {last_book.title} by {last_book.author}')
```

### Method 5: Using Book.objects.values() for specific fields
```python
from bookshelf.models import Book

# Get only specific fields
book_titles = Book.objects.values('title', 'author')

print('Book titles and authors:')
for book in book_titles:
    print(f"Title: {book['title']}, Author: {book['author']}")
```

## Expected Output

### Method 1 Output (objects.get)
```
Book retrieved successfully using objects.get()!
ID: 8
Title: 1984
Author: George Orwell
Publication Year: 1949
String representation: 1984
```

### Method 2 Output (objects.all)
```
Retrieved 6 books:
ID: 2, Title: To Kill a Mockingbird, Author: Harper Lee, Year: 1960
ID: 3, Title: 1984, Author: George Orwell, Year: 1949
ID: 4, Title: Pride and Prejudice, Author: Jane Austen, Year: 1813
ID: 5, Title: The Great Gatsby, Author: F. Scott Fitzgerald, Year: 1925
ID: 6, Title: Animal Farm, Author: George Orwell, Year: 1945
ID: 8, Title: 1984, Author: George Orwell, Year: 1949
```

### Method 3 Output (objects.filter)
```
Books by George Orwell (3 found):
ID: 3, Title: 1984, Year: 1949
ID: 6, Title: Animal Farm, Year: 1945
ID: 8, Title: 1984, Year: 1949

Books published in 1949 (2 found):
ID: 3, Title: 1984, Author: George Orwell
ID: 8, Title: 1984, Author: George Orwell
```

### Method 4 Output (objects.first/last)
```
First book: To Kill a Mockingbird by Harper Lee
Last book: 1984 by George Orwell
```

### Method 5 Output (objects.values)
```
Book titles and authors:
Title: To Kill a Mockingbird, Author: Harper Lee
Title: 1984, Author: George Orwell
Title: Pride and Prejudice, Author: Jane Austen
Title: The Great Gatsby, Author: F. Scott Fitzgerald
Title: Animal Farm, Author: George Orwell
Title: 1984, Author: George Orwell
```

## Explanation

### Method 1: Book.objects.get()
- **Purpose**: Retrieve a single object by unique identifier
- **Returns**: Single Book instance
- **Use Case**: When you know the exact ID or unique field value
- **Note**: Raises `DoesNotExist` if no object found, `MultipleObjectsReturned` if multiple objects found

### Method 2: Book.objects.all()
- **Purpose**: Retrieve all objects from the database
- **Returns**: QuerySet containing all Book instances
- **Use Case**: When you need to work with all records
- **Performance**: Use with caution on large datasets

### Method 3: Book.objects.filter()
- **Purpose**: Retrieve objects matching specific criteria
- **Returns**: QuerySet (can be empty, single, or multiple objects)
- **Use Case**: When you need to find objects based on field values
- **Flexibility**: Supports complex queries with multiple conditions

### Method 4: Book.objects.first() / Book.objects.last()
- **Purpose**: Get the first or last object (by ordering)
- **Returns**: Single Book instance or None if no objects exist
- **Use Case**: Quick access to boundary records
- **Safety**: Returns None instead of raising exceptions

### Method 5: Book.objects.values()
- **Purpose**: Retrieve only specific fields as dictionaries
- **Returns**: QuerySet of dictionaries
- **Use Case**: When you only need certain fields (performance optimization)
- **Benefit**: Reduces memory usage and database load

## Objects Manager Methods Summary

| Method | Purpose | Returns | Use Case |
|--------|---------|---------|----------|
| `objects.get()` | Single object by criteria | Book instance | Exact match needed |
| `objects.all()` | All objects | QuerySet | Need all records |
| `objects.filter()` | Objects matching criteria | QuerySet | Conditional retrieval |
| `objects.first()` | First object | Book instance or None | Quick access to first |
| `objects.last()` | Last object | Book instance or None | Quick access to last |
| `objects.values()` | Specific fields only | Dict QuerySet | Performance optimization |

## Result
- Successfully demonstrated multiple retrieval methods using Django's objects manager
- Each method serves different use cases and performance requirements
- All methods leverage Django ORM for database abstraction
- QuerySets are lazy-loaded and can be chained for complex queries
