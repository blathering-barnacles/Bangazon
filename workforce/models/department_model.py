from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import HARD_DELETE_NOCASCADE

class Department(models.Model, SafeDeleteModel):
    """

    Summary:
        This class creates the Department table

    Author:
        Dillon Williams

    methods:
        __str__: computes the “informal” or nicely printable string representation of an object. The return value must be a string object.

    """
    _safedelete_policy = HARD_DELETE_NOCASCADE
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