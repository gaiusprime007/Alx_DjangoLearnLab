from django.db import models

# Create your models here.
#PARENT MODEL
class Author(models.Model):
    name=models.CharField(max_length=100)


#CHILD MODEL
class Book(models.Model):
    title=models.CharField(max_length=100)  #title of the book
    publication_year=models.IntegerField() #publication year of the book
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author') #author of the book --> ForeignKey to Author model