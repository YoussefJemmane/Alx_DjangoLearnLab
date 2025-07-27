from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book, CustomUser
from .forms import BookForm, ExampleForm

# Create your views here.

# Permission-based views for Book model

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    Display list of books. Requires 'can_view' permission.
    """
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_detail(request, pk):
    """
    Display details of a specific book. Requires 'can_view' permission.
    """
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/book_detail.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    """
    Create a new book. Requires 'can_create' permission.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Book "{book.title}" created successfully!')
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form, 'title': 'Create Book'})

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    """
    Edit an existing book. Requires 'can_edit' permission.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Book "{book.title}" updated successfully!')
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form, 'book': book, 'title': 'Edit Book'})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    """
    Delete a book. Requires 'can_delete' permission.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book_title = book.title
        book.delete()
        messages.success(request, f'Book "{book_title}" deleted successfully!')
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

# Class-based views with permission mixins

class BookListView(PermissionRequiredMixin, ListView):
    """
    Class-based view for listing books with permission requirement.
    """
    model = Book
    template_name = 'bookshelf/book_list.html'
    context_object_name = 'books'
    permission_required = 'bookshelf.can_view'
    
class BookCreateView(PermissionRequiredMixin, CreateView):
    """
    Class-based view for creating books with permission requirement.
    """
    model = Book
    form_class = BookForm
    template_name = 'bookshelf/book_form.html'
    permission_required = 'bookshelf.can_create'
    success_url = reverse_lazy('book_list')
    
    def form_valid(self, form):
        messages.success(self.request, f'Book "{form.instance.title}" created successfully!')
        return super().form_valid(form)

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Class-based view for updating books with permission requirement.
    """
    model = Book
    form_class = BookForm
    template_name = 'bookshelf/book_form.html'
    permission_required = 'bookshelf.can_edit'
    success_url = reverse_lazy('book_list')
    
    def form_valid(self, form):
        messages.success(self.request, f'Book "{form.instance.title}" updated successfully!')
        return super().form_valid(form)

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Class-based view for deleting books with permission requirement.
    """
    model = Book
    template_name = 'bookshelf/book_confirm_delete.html'
    permission_required = 'bookshelf.can_delete'
    success_url = reverse_lazy('book_list')
    
    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        messages.success(request, f'Book "{book.title}" deleted successfully!')
        return super().delete(request, *args, **kwargs)

# Security-focused example view with input validation
@login_required
def secure_book_search(request):
    """
    Secure search functionality that prevents SQL injection.
    Uses Django ORM for safe database queries.
    """
    books = []
    query = None
    
    if request.method == 'GET' and 'q' in request.GET:
        # Get and sanitize user input
        query = request.GET.get('q', '').strip()
        
        if query:
            # Use Django ORM to prevent SQL injection
            # Instead of raw SQL: "SELECT * FROM books WHERE title LIKE '%{}%'".format(query)
            # We use Django's safe ORM methods:
            books = Book.objects.filter(
                title__icontains=query
            ).distinct()[:50]  # Limit results to prevent performance issues
    
    return render(request, 'bookshelf/book_search.html', {
        'books': books,
        'query': query
    })

# Example Form View demonstrating security features
def form_example(request):
    """
    Example view demonstrating secure form handling.
    Includes CSRF protection, input validation, and XSS prevention.
    """
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the cleaned data safely
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # In a real application, you would save this data or send an email
            messages.success(
                request, 
                f'Thank you {name}! Your message has been received. '
                f'We will contact you at {email} if needed.'
            )
            return redirect('form_example')  # Redirect after POST to prevent re-submission
    else:
        form = ExampleForm()
    
    return render(request, 'bookshelf/form_example.html', {'form': form})
