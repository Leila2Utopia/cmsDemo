from django.db import models
import time
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    create_time = models.DateTimeField()
    memo = models.CharField(max_length=32, default="")

    publish = models.ForeignKey(to="Publish", default=1)
    author = models.ManyToManyField("Author")

    def __str__(self):return self.title


class Publish(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)

class Author(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):return self.name

