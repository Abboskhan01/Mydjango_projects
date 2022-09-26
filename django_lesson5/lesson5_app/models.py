from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    phone_number = models.IntegerField(max_length=10, null=True, blank=True)
    email = models.EmailField()
    course_type = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
