from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.utils.decorators import method_decorator
from .models import Book, Author
from .models import Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details
class LibraryDetailView(ListView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_queryset(self):
        # Get a specific library or the first one if no pk is provided
        if 'pk' in self.kwargs:
            return Library.objects.filter(pk=self.kwargs['pk'])
        return Library.objects.all()[:1]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context['library']:
            context['library'] = context['library'][0]
        return context

# Role-based views

# A decorator to check if the user has a specific role

def role_required(role):
    def has_role(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return user_passes_test(has_role)

# Views for Admin
@role_required('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Views for Librarian
@role_required('Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Views for Member
@role_required('Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Authentication Views
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Permission-secured views for book operations

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_name = request.POST.get('author')
        if title and author_name:
            author, created = Author.objects.get_or_create(name=author_name)
            book = Book.objects.create(title=title, author=author)
            messages.success(request, f'Book "{title}" added successfully!')
            return redirect('list_books')
        else:
            messages.error(request, 'Please provide both title and author.')
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book_view(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        messages.error(request, 'Book not found.')
        return redirect('list_books')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        author_name = request.POST.get('author')
        if title and author_name:
            author, created = Author.objects.get_or_create(name=author_name)
            book.title = title
            book.author = author
            book.save()
            messages.success(request, f'Book "{title}" updated successfully!')
            return redirect('list_books')
        else:
            messages.error(request, 'Please provide both title and author.')
    
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book_view(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        messages.error(request, 'Book not found.')
        return redirect('list_books')
    
    if request.method == 'POST':
        book_title = book.title
        book.delete()
        messages.success(request, f'Book "{book_title}" deleted successfully!')
        return redirect('list_books')
    
    return render(request, 'relationship_app/delete_book.html', {'book': book})
