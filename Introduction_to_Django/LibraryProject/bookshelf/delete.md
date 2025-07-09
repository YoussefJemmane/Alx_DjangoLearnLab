# DELETE Operation

## Objective
Delete the book created and confirm the deletion by trying to retrieve all books again.

## Django Shell Commands
```python
from bookshelf.models import Book

# Show all books before deletion
print('Before deletion:')
all_books = Book.objects.all()
print(f'Total number of books: {all_books.count()}')
for book in all_books:
    print(f'ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.publication_year}')

# Find and delete the specific book
book_to_delete = Book.objects.get(id=7)
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
    deleted_book = Book.objects.get(id=7)
    print(f'Book still exists: {deleted_book.title}')
except Book.DoesNotExist:
    print('\nConfirmation: Book with ID 7 no longer exists in the database')

print('\nDeletion completed successfully!')
```

## Expected Output
```
Before deletion:
Total number of books: 6
ID: 2, Title: To Kill a Mockingbird, Author: Harper Lee, Year: 1960
ID: 3, Title: 1984, Author: George Orwell, Year: 1949
ID: 4, Title: Pride and Prejudice, Author: Jane Austen, Year: 1813
ID: 5, Title: The Great Gatsby, Author: F. Scott Fitzgerald, Year: 1925
ID: 6, Title: Animal Farm, Author: George Orwell, Year: 1945
ID: 7, Title: Nineteen Eighty-Four, Author: George Orwell, Year: 1949

Deleting book: Nineteen Eighty-Four by George Orwell

After deletion:
Total number of books: 5
ID: 2, Title: To Kill a Mockingbird, Author: Harper Lee, Year: 1960
ID: 3, Title: 1984, Author: George Orwell, Year: 1949
ID: 4, Title: Pride and Prejudice, Author: Jane Austen, Year: 1813
ID: 5, Title: The Great Gatsby, Author: F. Scott Fitzgerald, Year: 1925
ID: 6, Title: Animal Farm, Author: George Orwell, Year: 1945

Confirmation: Book with ID 7 no longer exists in the database

Deletion completed successfully!
```

## Explanation
1. **Import Model**: Import the Book model from bookshelf.models
2. **Show Before State**: Display all books in the database before deletion
3. **Retrieve Target**: Get the specific book with ID 7 to delete
4. **Delete Object**: Call `book.delete()` to remove the object from the database
5. **Show After State**: Display all remaining books after deletion
6. **Confirm Deletion**: Try to retrieve the deleted book to confirm it no longer exists
7. **Handle Exception**: Use try-except to catch `Book.DoesNotExist` exception

## Result
- Successfully deleted the Book instance with ID 7 ("Nineteen Eighty-Four")
- Total book count reduced from 6 to 5
- The deleted book no longer appears in the database
- Attempting to retrieve the deleted book raises `Book.DoesNotExist` exception
- All other books remain unchanged in the database
- Deletion is permanently committed to the database
