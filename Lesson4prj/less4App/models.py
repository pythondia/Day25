from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    did = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department')

    def __str__(self):
        return self.name
