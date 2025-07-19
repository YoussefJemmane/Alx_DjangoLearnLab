from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for these fields in the admin sidebar
    list_filter = ('author', 'publication_year')
    
    # Enable search functionality for these fields
    search_fields = ('title', 'author')
    
    # Optional: Add ordering
    ordering = ('title',)

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)
