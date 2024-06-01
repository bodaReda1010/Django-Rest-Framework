from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    birth_date = models.DateField()

    class Meta:
        verbose_name = ("Author")
        verbose_name_plural = ("Authors")

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author , on_delete=models.CASCADE)
    publish_date = models.DateField()
    price = models.IntegerField()

    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")

    def __str__(self):
        return self.title
    

class Review(models.Model):
    book = models.ForeignKey(Book , on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=50)
    review = models.TextField()
    rate = models.CharField(max_length=50 , choices=[(i , i) for i in range(1 , 6)])

    class Meta:
        verbose_name = ("Review")
        verbose_name_plural = ("Reviews")

    def __str__(self):
        return self.book
