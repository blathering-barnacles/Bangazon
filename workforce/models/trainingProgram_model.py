from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import HARD_DELETE_NOCASCADE


class TrainingProgram(SafeDeleteModel):
    """
    A model that defines a Training Program and will create a table in our database with the same name
    Author: S.W., R.L.
    methods: __str__
    """

    _safedelete_policy = HARD_DELETE_NOCASCADE
    name = models.CharField(max_length=35)
    startDate = models.DateField()
    endDate = models.DateField()
    maxAttendees = models.IntegerField()
    employee = models.ManyToManyField("Employee", through='EmployeeTrainingProgram')

    def __str__(self):
        ''' returns a string representation of the model '''
        return self.name



