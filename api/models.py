from django.db import models


class Author(models.Model):

    first_name =  models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=10)

class Book(models.Model):

    title = models.CharField(max_length=30)
    subject = models.CharField(max_length=15)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
