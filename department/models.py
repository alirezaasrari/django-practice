from django.db import models

class Department(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    position = models.ForeignKey(Department, on_delete = models.CASCADE, blank = True, null = True)
    name = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    age = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['age']


