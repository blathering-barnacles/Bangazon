from django.db import models

class Employee(models.Model):
    """

    Summary:
        This class creates the Employee table

    Author: 
        Dillon Williams
    
    methods:
        __str__: computes the “informal” or nicely printable string representation of an object. The return value must be a string object.

    """

    department = models.ForeignKey("Department", on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    startDate = models.DateField()
    isSupervisor = models.BooleanField()

    def __str__(self):
        """

    Purpose: 
        converts data to string,
    Arguments: 
        self: The first argument of every class method, including init, is always a reference to the current instance of the class. By convention, this argument is always named 'self'. 

        """
        return self.firstName, self.lastName

