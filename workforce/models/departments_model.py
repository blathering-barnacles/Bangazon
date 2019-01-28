from django.db import models

class Department(models.Model):
    """
    
    This creates the Department table
    
    Author: Dillon Williams
    methods: 
        __str__:
    
    """ 

    name = models.CharField(max_length=100)
    budget = models.IntegerField()

    """
    
    Purpose: converts data to string, 
    Arguments: self
    
    """

    def __str__(self):
        return self.name