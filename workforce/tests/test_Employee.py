import unittest
from django.test import TestCase
from django.urls import reverse
from django.utils.dateparse import parse_date
from ..models import Employee, Department
import datetime

class EmployeeTest(TestCase):

    def test_detail(self):

        new_department = Department.objects.create(
            name = "HR",
            budget = 2000
        )

        new_employee = Employee.objects.create(
            firstName = "Wally",
            lastName = "Barnett",
            startDate = "2019-01-03",
            isSupervisor  = 0,
            department = new_department
        )


        response = self.client.get(reverse('workforce:employeeDetail', args=(1,)))
        self.assertIn(new_employee.firstName.encode(), response.content)
        self.assertIn(new_employee.lastName.encode(), response.content)
        self.assertIn(new_employee.department.name.encode(), response.content)
