from django import forms
from django.core.exceptions import ValidationError
from .models import Book, CustomUser

class BookForm(forms.ModelForm):
    """
    Secure form for Book model with input validation and CSRF protection.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book title',
                'maxlength': 200
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter author name',
                'maxlength': 100
            }),
            'publication_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter publication year',
                'min': 1000,
                'max': 2024
            })
        }
    
    def clean_title(self):
        """Validate and sanitize book title."""
        title = self.cleaned_data.get('title')
        if title:
            title = title.strip()
            if len(title) < 2:
                raise ValidationError("Title must be at least 2 characters long.")
            # Basic XSS prevention - remove potentially harmful characters
            dangerous_chars = ['<', '>', '"', "'", '&']
            for char in dangerous_chars:
                if char in title:
                    raise ValidationError("Title contains invalid characters.")
        return title
    
    def clean_author(self):
        """Validate and sanitize author name."""
        author = self.cleaned_data.get('author')
        if author:
            author = author.strip()
            if len(author) < 2:
                raise ValidationError("Author name must be at least 2 characters long.")
            # Basic XSS prevention
            dangerous_chars = ['<', '>', '"', "'", '&']
            for char in dangerous_chars:
                if char in author:
                    raise ValidationError("Author name contains invalid characters.")
        return author
    
    def clean_publication_year(self):
        """Validate publication year."""
        year = self.cleaned_data.get('publication_year')
        if year:
            if year < 1000 or year > 2024:
                raise ValidationError("Publication year must be between 1000 and 2024.")
        return year

class SecureSearchForm(forms.Form):
    """
    Secure search form with input validation to prevent injection attacks.
    """
    query = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search for books...',
            'maxlength': 100
        })
    )
    
    def clean_query(self):
        """Sanitize and validate search query."""
        query = self.cleaned_data.get('query')
        if query:
            query = query.strip()
            # Remove potentially dangerous characters for XSS prevention
            dangerous_chars = ['<', '>', '"', "'", '&', ';', '--']
            for char in dangerous_chars:
                query = query.replace(char, '')
            # Limit length to prevent DoS attacks
            if len(query) > 100:
                query = query[:100]
        return query

class CustomUserCreationForm(forms.ModelForm):
    """
    Secure form for creating CustomUser instances.
    """
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'date_of_birth']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
    
    def clean_password2(self):
        """Validate password confirmation."""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        """Save user with encrypted password."""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
