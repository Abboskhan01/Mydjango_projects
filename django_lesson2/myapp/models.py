from django.db import models


# Create your models here.


class Author(models.Model):
    firstname = models.CharField(max_length=100, blank=False, null=False)
    lastname = models.CharField(max_length=100, blank=False, null=False)
    age = models.SmallIntegerField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    author = models.ForeignKey(Author, null=False, blank=False, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Person(models.Model):
    Sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    name = models.CharField(max_length=100)
    shirt_size = models.CharField(max_length=100, choices=Sizes)

    def __str__(self):
        return self.name
