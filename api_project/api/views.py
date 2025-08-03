from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# ListView for basic API endpoint - returns all books
class BookList(generics.ListAPIView):
    """
    API view to retrieve a list of all books.
    Requires authentication to access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# ViewSet for full CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    Requires authentication to access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
