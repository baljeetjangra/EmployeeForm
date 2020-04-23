from django.db import models

# Create your models here.


class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Employee(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    emp_code = models.CharField(max_length=5)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname

