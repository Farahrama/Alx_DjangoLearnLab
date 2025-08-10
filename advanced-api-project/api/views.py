from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter  # Ensure SearchFilter and OrderingFilter are correctly imported
from django_filters import rest_framework as filters  # Ensure filters is correctly imported
from .models import Book
from .serializers import BookSerializer


class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Ensure filters.OrderingFilter and filters.SearchFilter are included exactly as required
    filter_backends = [filters.DjangoFilterBackend, SearchFilter, OrderingFilter]  # Correct usage of filters.OrderingFilter and filters.SearchFilter
    filterset_fields = ['title', 'author', 'publication_year']  # Filtering fields
    search_fields = ['title', 'author']  # Search fields
    ordering_fields = ['title', 'publication_year']  # Ordering fields
# Create your views here.
