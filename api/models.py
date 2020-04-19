from django.db import models


class Book(models.Model):

    title = models.CharField(max_length=30)
    subject = models.CharField(max_length=15)
    author = models.CharField(max_length=30)
