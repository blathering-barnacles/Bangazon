import unittest
from django.test import TestCase
from django.urls import reverse
from ..models import Department, Employee


class DepartmentDetailTest(TestCase):

    def test_list_departments(self):
        new_department1 = Department.objects.create(
            name="Fuck we need a hugh",
            budget="4000")


        new_department2 = Department.objects.create(
            name="Yes we do",
            budget="5000")

        # new_employee = Employee.objects.create(
        #     department=new_department,
        #     firstName="Fonz",
        #     lastName="Mirand",
        #     startDate="1992-08-21",
        #     isSupervisor=1
        # )

        # print(new_department)

        # Issue a GET request. "client" is a dummy web browser
        # 'reverse' is used to generate a URL for a given view. The main advantage is that you do not hard code routes in your code.
        response = self.client.get(reverse('workforce:departmentDetail', args=(1,)))
        print(response.content)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)


        # Check that the rendered context contains 1 artist.
        # Response.context is the context variable passed to the template by the view. This is incredibly useful for testing, because it allows us to confirm that our template is getting all the data it needs.

        print(len(response.context['departments']))
        # self.assertEqual(len(response.context['departments']), 2)