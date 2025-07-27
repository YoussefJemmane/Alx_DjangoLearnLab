from django.urls import path
from . import views

# URL patterns for bookshelf app with permission-based access control
urlpatterns = [
    # Book management URLs with permission enforcement
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
    
    # Class-based view alternatives (commented out to avoid conflicts)
    # path('books/cbv/', views.BookListView.as_view(), name='book_list_cbv'),
    # path('books/cbv/create/', views.BookCreateView.as_view(), name='book_create_cbv'),
    # path('books/cbv/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_edit_cbv'),
    # path('books/cbv/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete_cbv'),
    
    # Security-focused search functionality
    path('books/search/', views.secure_book_search, name='book_search'),
    
    # Example form demonstrating security features
    path('form-example/', views.form_example, name='form_example'),
]
