from django.db import models
from .employee_model import Employee
from .trainingProgram_model import TrainingProgram

class EmployeeTrainingProgram(models.Model):
    """
    A model that defines a many-to-many relationship between our Employee and Training Program models and will create a table in our database
    Author: S.W., R.L.
    methods: null
    """
    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    trainingProgram = models.ForeignKey("TrainingProgram", on_delete=models.CASCADE)

