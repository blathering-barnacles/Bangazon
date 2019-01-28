from django.db import models

class EmployeeTrainingProgram(models.Model):
    """
    A model that defines a many-to-many relationship between our Employee and Training Program models and will create a table in our database
    Author: S.W., R.L.
    methods: null
    """
    employeeId = models.ForeignKey("Employee", on_delete=models.CASCADE)
    trainingProgramId = models.ForeignKey("TrainingProgram", on_delete=models.CASCADE)

