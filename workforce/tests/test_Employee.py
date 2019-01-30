import unittest
from django.test import TestCase
from django.urls import reverse
from django.utils.dateparse import parse_date
from ..models import Employee, Department, TrainingProgram, EmployeeTrainingProgram
import datetime

class EmployeeTest(TestCase):
    '''
    This tests the Employee table

    Authors: J.Barnett,
    '''

    def test_detail(self):
        '''[adds new employee, department, training, and employeeTraining relationship to the virtual database and confirms that the response contains the employee's first name, last name, department name and training program]
        '''

        new_department = Department.objects.create(
            name = "HR",
            budget = 2000
        )

        new_training = TrainingProgram.objects.create(
            name = "React Components",
            startDate = "2017-02-02",
            endDate = "2017-02-04",
            maxAttendees = 10
        )

        new_employee = Employee.objects.create(
            firstName = "Wally",
            lastName = "Barnett",
            startDate = "2019-01-03",
            isSupervisor  = 0,
            department = new_department
        )

        new_registration = EmployeeTrainingProgram.objects.create(
            employee = new_employee,
            trainingProgram = new_training
        )


        response = self.client.get(reverse('workforce:employeeDetail', args=(1,)))
        self.assertIn(new_employee.firstName.encode(), response.content)
        self.assertIn(new_employee.lastName.encode(), response.content)
        self.assertIn(new_employee.department.name.encode(), response.content)
        self.assertEqual(response.context["training_programs"][0].trainingProgram.name, new_training.name)