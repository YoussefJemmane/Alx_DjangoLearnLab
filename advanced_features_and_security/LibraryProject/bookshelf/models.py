from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone

# Create your models here.

class CustomUserManager(BaseUserManager):
    """
    Custom user manager for CustomUser model.
    Handles creation of regular users and superusers with custom fields.
    """
    def create_user(self, username, email=None, password=None, **extra_fields):
        """
        Create and return a regular user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The Username field must be set')
        
        email = self.normalize_email(email) if email else None
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """
        Create and return a superuser with the given username, email, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    """
    Custom user model extending AbstractUser with additional fields.
    Includes date_of_birth and profile_photo fields for enhanced user profiles.
    """
    date_of_birth = models.DateField(
        null=True, 
        blank=True, 
        help_text="User's date of birth"
    )
    profile_photo = models.ImageField(
        upload_to='profile_photos/', 
        null=True, 
        blank=True,
        help_text="User's profile photo"
    )
    
    objects = CustomUserManager()
    
    class Meta:
        # Custom permissions for user management
        permissions = [
            ('can_view', 'Can view user'),
            ('can_create', 'Can create user'),
            ('can_edit', 'Can edit user'),
            ('can_delete', 'Can delete user'),
        ]
    
    def __str__(self):
        return self.username
    
    def get_age(self):
        """Calculate and return user's age based on date_of_birth."""
        if self.date_of_birth:
            today = timezone.now().date()
            return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
        return None

class Book(models.Model):
    """
    Book model with custom permissions for content management.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    class Meta:
        # Custom permissions for book management
        permissions = [
            ('can_view', 'Can view book'),
            ('can_create', 'Can create book'),
            ('can_edit', 'Can edit book'),
            ('can_delete', 'Can delete book'),
        ]

    def __str__(self):
        return self.title
