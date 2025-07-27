from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import CustomUser, Book

# Custom User Admin Configuration
class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface for CustomUser model.
    Extends Django's UserAdmin to handle additional fields.
    """
    # Fields to display in the user list view
    list_display = (
        'username', 'email', 'first_name', 'last_name', 
        'date_of_birth', 'is_staff', 'is_active', 'date_joined'
    )
    
    # Fields to filter by in the admin sidebar
    list_filter = (
        'is_staff', 'is_superuser', 'is_active', 'date_joined', 'date_of_birth'
    )
    
    # Fields to search by
    search_fields = ('username', 'first_name', 'last_name', 'email')
    
    # Organize fields in the user detail/edit view
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'profile_photo')
        }),
    )
    
    # Fields to include when adding a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'profile_photo')
        }),
    )
    
    # Ordering of users in the list view
    ordering = ('username',)

class BookAdmin(admin.ModelAdmin):
    """
    Enhanced admin interface for Book model with permission-based features.
    """
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for these fields in the admin sidebar
    list_filter = ('author', 'publication_year')
    
    # Enable search functionality for these fields
    search_fields = ('title', 'author')
    
    # Optional: Add ordering
    ordering = ('title',)
    
    # Define which permissions are required for different actions
    def has_view_permission(self, request, obj=None):
        """Check if user has permission to view book."""
        return request.user.has_perm('bookshelf.can_view') or super().has_view_permission(request, obj)
    
    def has_add_permission(self, request):
        """Check if user has permission to add book."""
        return request.user.has_perm('bookshelf.can_create') or super().has_add_permission(request)
    
    def has_change_permission(self, request, obj=None):
        """Check if user has permission to change book."""
        return request.user.has_perm('bookshelf.can_edit') or super().has_change_permission(request, obj)
    
    def has_delete_permission(self, request, obj=None):
        """Check if user has permission to delete book."""
        return request.user.has_perm('bookshelf.can_delete') or super().has_delete_permission(request, obj)

# Register models with their respective admin classes
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book, BookAdmin)

# Customize admin site headers
admin.site.site_header = "Library Management System"
admin.site.site_title = "Library Admin"
admin.site.index_title = "Welcome to Library Administration"
