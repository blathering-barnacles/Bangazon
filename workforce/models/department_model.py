from django.db import models

class Department(models.Model):
    """

    Summary:
        This class creates the Department table

    Author:
        Dillon Williams

    methods:
        __str__: computes the “informal” or nicely printable string representation of an object. The return value must be a string object.

    """

    name = models.CharField(max_length=100)
    budget = models.IntegerField()

    """

    Purpose:
        converts data to string,
    Arguments:
        self: The first argument of every class method, including init, is always a reference to the current instance of the class. By convention, this argument is always named 'self'.

    """

    def __str__(self):
        return self.name