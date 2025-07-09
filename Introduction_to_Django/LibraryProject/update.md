# UPDATE Operation

## Command
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.title = 'Nineteen Eighty-Four'
book.save()
```

## Expected Output
```
Before update:
Title: 1984
After update:
Title: Nineteen Eighty-Four
Book updated successfully!
```

## Description
This command updates the title of the Book instance with ID 1:
- **Before**: "1984"
- **After**: "Nineteen Eighty-Four"

The process involves:
1. Retrieving the book object using `Book.objects.get(id=1)`
2. Modifying the title attribute
3. Saving the changes to the database using `book.save()`

The update is confirmed by displaying the title before and after the modification.
