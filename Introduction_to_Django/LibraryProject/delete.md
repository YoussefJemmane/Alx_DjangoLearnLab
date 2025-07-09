# DELETE Operation

## Command
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.delete()

# Confirm deletion
books = Book.objects.all()
print(f'Number of books: {books.count()}')
```

## Expected Output
```
Before deletion:
Number of books: 1
Book: Nineteen Eighty-Four by George Orwell
Book deleted successfully!
After deletion:
Number of books: 0
No books found in database
```

## Description
This command deletes the Book instance with ID 1 from the database:

**Before deletion:**
- Number of books: 1
- Book: "Nineteen Eighty-Four" by George Orwell

**After deletion:**
- Number of books: 0
- No books found in database

The process involves:
1. Retrieving the book object using `Book.objects.get(id=1)`
2. Deleting the object using `book.delete()`
3. Confirming the deletion by querying all books with `Book.objects.all()`

The deletion is confirmed by showing that the book count reduced from 1 to 0.
