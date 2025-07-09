# UPDATE Operation

## Objective
Update the title of "1984" to "Nineteen Eighty-Four" and save the changes.

## Django Shell Commands
```python
from bookshelf.models import Book

# Retrieve the book with ID 7
book = Book.objects.get(id=7)

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

## Expected Output
```
Before update:
ID: 7
Title: 1984
Author: George Orwell
Publication Year: 1949

After update:
ID: 7
Title: Nineteen Eighty-Four
Author: George Orwell
Publication Year: 1949
String representation: Nineteen Eighty-Four

Update completed successfully!
```

## Explanation
1. **Import Model**: Import the Book model from bookshelf.models
2. **Retrieve Object**: Use `Book.objects.get(id=7)` to fetch the specific book
3. **Show Before State**: Display all attributes before the update
4. **Modify Attribute**: Change the title from "1984" to "Nineteen Eighty-Four"
5. **Save Changes**: Call `book.save()` to persist the changes to the database
6. **Show After State**: Display all attributes after the update
7. **Confirm Update**: The string representation also changes to reflect the new title

## Result
- Successfully updated the Book instance with ID 7
- Title changed from "1984" to "Nineteen Eighty-Four"
- All other attributes remain unchanged (ID: 7, Author: George Orwell, Publication Year: 1949)
- The string representation now shows "Nineteen Eighty-Four"
- Changes are persisted in the database
