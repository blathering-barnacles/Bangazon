from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    budget = models.IntegerField()

    def __str__(self):
        return self.name