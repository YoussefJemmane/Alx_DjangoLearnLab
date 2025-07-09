# Django Admin Quick Reference

## Access Admin Interface
1. **Start server**: `python3 manage.py runserver`
2. **URL**: `http://localhost:8000/admin/`
3. **Login**: admin / [your_password]

## Current Admin Configuration

### Book Model Admin Features
- **List Display**: Title, Author, Publication Year
- **Filters**: Author, Publication Year
- **Search**: Title, Author
- **Ordering**: Alphabetical by title

## Quick Actions

### View All Books
- Go to admin dashboard
- Click "Books" under BOOKSHELF section

### Add New Book
- Click "Add" button next to Books
- Fill in: Title, Author, Publication Year
- Click "Save"

### Edit Book
- Click on book title in list view
- Modify fields as needed
- Click "Save"

### Delete Book
- Select book(s) using checkboxes
- Choose "Delete selected books" from Actions dropdown
- Click "Go"

### Filter Books
- Use sidebar filters:
  - By Author
  - By Publication Year

### Search Books
- Use search box at top
- Searches in title and author fields

## Sample Data Available
- To Kill a Mockingbird (Harper Lee, 1960)
- 1984 (George Orwell, 1949)
- Pride and Prejudice (Jane Austen, 1813)
- The Great Gatsby (F. Scott Fitzgerald, 1925)
- Animal Farm (George Orwell, 1945)

## Testing Checklist
- [ ] Access admin interface
- [ ] View book list with custom columns
- [ ] Test author filter
- [ ] Test publication year filter
- [ ] Test search functionality
- [ ] Add new book
- [ ] Edit existing book
- [ ] Delete book
- [ ] Verify alphabetical ordering
