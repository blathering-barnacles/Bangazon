from django.db import models

class Employee(models.Model):
    departmentId = models.ForeignKey(Department, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    startDate = models.DateTimeField()
    isSupervisor = models.BooleanField()
    
