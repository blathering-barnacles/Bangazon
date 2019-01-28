from django.db import models

class Employee(models.Model):
    """
    
    This creates the Department table
    
    Author: Dillon Williams
    methods: 
        __str__:
    
    """ 

    departmentId = models.ForeignKey(Department, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    startDate = models.DateTimeField()
    isSupervisor = models.BooleanField()

    """
    
    Purpose: converts data to string, 
    Arguments: self
    
    """
    def __str__(self):
        return self.firstName, self.lastName
    
