from django.db import models


# Note to self: Only the main class has the many to many, the join table has both foreing keys.
# The many to many will access the join table and get the foreing keys that it needs from the join table.

class Computer(models.Model):
    ''' 
    description: This class creates a computer and its properties.
    author: Alfonso Miranda.
    method: there is a string method that just returns the make.
    properties:
      make = The make will contain the name of the brand of the computer.
      purchaseDate = This property contains the purchase date in string form.
      decomissionDate = This property contains the dicomission date in string form.
      employees = This property contains the many to many relationship with the computer/employee model.
    '''
    make = models.CharField(max_length=20)
    purchaseDate = models.DateField()
    decommissionDate = models.DateField()
    employees = models.ManyToManyField("Employee", through='ComputerEmployee')

    def __str__(self):
        ''' purpose: This method just returns the make. arguments: self '''
        return self.make