from django.shortcuts import render
from api import serializers
from .models import Book
from rest_framework import generics
from rest_framework import permissions

# Create your views here.

#viie to retrieve all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [permissions.AllowAny]

#view to retrieve a specific book by its ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [permissions.AllowAny]
    

#CreateAPIView to add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.is_valided(raise_exception=True)
        serializer.save()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response



#MOodify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Book.objects.filter(publication_year__lte=2024)  # Example filter: only allow updates to books published in or before 2024

    def perform_update(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return response
   

#Delete an existing book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [permissions.IsAuthenticated]
   