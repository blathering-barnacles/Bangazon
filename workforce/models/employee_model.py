from django.db import models

class Employee(models.Model):
    """

    This creates the Employee table

    Author: Dillon Williams
    methods:
        __str__:

    """

    department = models.ForeignKey("Department", on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    startDate = models.DateField()
    isSupervisor = models.BooleanField()

    def __str__(self):
        """

        Purpose: converts data to string,
        Arguments: self

        """
        return self.firstName, self.lastName

