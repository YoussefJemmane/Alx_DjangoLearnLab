from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList, BookViewSet

# Create a router and register our ViewSet with it
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# The API URLs are now determined automatically by the router
urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),
    
    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),
    
    # Authentication endpoint for obtaining tokens
    path('auth/token/', obtain_auth_token, name='api_token_auth'),
]
