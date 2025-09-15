from django.db import models
<<<<<<< HEAD
=======
import django_filters
>>>>>>> 77bd30d4b0fbae909c372c6ad3f98a96820c6f30

# Create your models here.
#PARENT MODEL
class Author(models.Model):
    name=models.CharField(max_length=100)


#CHILD MODEL
class Book(models.Model):
    title=models.CharField(max_length=100)  #title of the book
    publication_year=models.IntegerField() #publication year of the book
<<<<<<< HEAD
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author') #author of the book --> ForeignKey to Author model
=======
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author') #author of the book --> ForeignKey to Author model

#Filter
class BookFilter(django_filters.FilterSet):
    title= django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    publication_year = django_filters.NumberFilter(field_name='publication_year', lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['publication_year']
    
>>>>>>> 77bd30d4b0fbae909c372c6ad3f98a96820c6f30
