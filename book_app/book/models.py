from django.db import models


class Author(models.Model):
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)

class Book(models.Model):
    name = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)



