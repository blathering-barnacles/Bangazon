from django.db import models

class ComputerEmployee(models.Model):
    """
    Creates the join table for the many to many relationship between computers and employees
    Author: J.Barnett
    methods: none
   """

    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    computer = models.ForeignKey("Computer", on_delete=models.CASCADE)
