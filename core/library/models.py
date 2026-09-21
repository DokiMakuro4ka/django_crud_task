from django.db import models

# Create your models here.

class Authors (models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    birth_date = models.DateField()

class Genres (models.Model):
    name = models.CharField(max_length=100)
    desciption = models.TextField()

class Books (models.Model):
    title = models.CharField(max_length=100)
    authors = models.ForeignKey(Authors, on_delete=models.CASCADE, related_name="books")
    isbn = models.CharField(max_length=100, unique=True)
    publication_year = models.IntegerField()
    genres = models.CharField(max_length=100)
    co_authors = models.CharField(max_length=100)
    summary = models.TextField()