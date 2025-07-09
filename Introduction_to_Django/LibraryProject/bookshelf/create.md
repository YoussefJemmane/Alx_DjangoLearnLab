# CREATE Operation

## Objective
Create a Book instance with the title "1984", author "George Orwell", and publication year 1949.

## Django Shell Commands
```python
from bookshelf.models import Book

# Create a new Book instance
book = Book(title='1984', author='George Orwell', publication_year=1949)
book.save()

# Display the created book details
print('Book created successfully!')
print(f'ID: {book.id}')
print(f'Title: {book.title}')
print(f'Author: {book.author}')
print(f'Publication Year: {book.publication_year}')
print(f'String representation: {str(book)}')
```

## Expected Output
```
Book created successfully!
ID: 7
Title: 1984
Author: George Orwell
Publication Year: 1949
String representation: 1984
```

## Explanation
1. **Import Model**: Import the Book model from bookshelf.models
2. **Create Instance**: Create a new Book object with the specified attributes
3. **Save to Database**: Call `save()` method to persist the object to the database
4. **Confirmation**: The book is assigned a unique ID (7) and all attributes are correctly stored
5. **String Representation**: The `__str__` method returns the book's title "1984"

## Result
- Successfully created a Book instance in the database
- The book has been assigned ID 7
- All attributes (title, author, publication_year) are correctly stored
- The object can be referenced using the `book` variable for further operations
