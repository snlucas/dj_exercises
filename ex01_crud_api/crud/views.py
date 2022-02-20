from rest_framework import generics

from books.models import Book
from .serializers import BookSerializer


class BookList(generics.ListCreateAPIView):
    # GET - POST method
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    # GET - UPDATE - DELETE methods
    queryset = Book.objects.all()
    serializer_class = BookSerializer
