# CREATE Operation

## Objective
Create a Book instance with the title "1984", author "George Orwell", and publication year 1949.

## Django Shell Commands

### Method 1: Using Book() constructor and save()
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

### Method 2: Using Book.objects.create()
```python
from bookshelf.models import Book

# Create and save a new Book instance in one step
book = Book.objects.create(
    title='1984',
    author='George Orwell',
    publication_year=1949
)

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

### Method 1: Constructor + save()
1. **Import Model**: Import the Book model from bookshelf.models
2. **Create Instance**: Create a new Book object with the specified attributes
3. **Save to Database**: Call `save()` method to persist the object to the database
4. **Confirmation**: The book is assigned a unique ID and all attributes are correctly stored
5. **String Representation**: The `__str__` method returns the book's title "1984"

### Method 2: Book.objects.create()
1. **Import Model**: Import the Book model from bookshelf.models
2. **Create and Save**: Use `Book.objects.create()` to create and save in one step
3. **Automatic Save**: The object is automatically saved to the database
4. **Return Object**: The method returns the created object with assigned ID
5. **String Representation**: The `__str__` method returns the book's title "1984"

## Differences Between Methods

| Aspect | Method 1 (Constructor + save) | Method 2 (objects.create) |
|--------|-------------------------------|---------------------------|
| **Steps** | Two steps: create, then save | One step: create and save |
| **Performance** | Slightly more control | More concise |
| **Use Case** | When you need to modify before saving | When you want to create and save immediately |
| **Validation** | Validation occurs during save() | Validation occurs during create() |

## Practical Example Output

### Using Book.objects.create()
```
Book created successfully using Book.objects.create()!
ID: 8
Title: 1984
Author: George Orwell
Publication Year: 1949
String representation: 1984
```

## Result
- Successfully created a Book instance in the database using either method
- The book is assigned a unique ID (e.g., ID 7 or 8)
- All attributes (title, author, publication_year) are correctly stored
- The object can be referenced using the `book` variable for further operations
- Both methods achieve the same result but with different approaches

## Best Practices

1. **Use `Book.objects.create()`** when you want to create and save in one step
2. **Use `Book() + save()`** when you need to perform operations before saving
3. **Both methods** handle validation and return the created object
4. **Choose based on your specific use case** and coding style preferences
