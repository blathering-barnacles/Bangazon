from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import HARD_DELETE_NOCASCADE
from .employee_model import Employee
from .trainingProgram_model import TrainingProgram


class EmployeeTrainingProgram(models.Model):
    """
    A model that defines a many-to-many relationship between our Employee and Training Program models and will create a table in our database
    Author: S.W., R.L.
    methods: null
    """
    # _safedelete_policy = HARD_DELETE_NOCASCADE
    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    trainingProgram = models.ForeignKey("TrainingProgram", on_delete=models.CASCADE)

