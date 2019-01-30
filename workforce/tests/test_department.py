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
        response2 = self.client.get(reverse('workforce:departmentDetail', args=(2,)))

        print("RESPONSE CONTENT: ", response.content)
        print("RESPONSE CONTEXT: ", response.context['departments'])

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['departments'].name, new_department1.name)
        self.assertEqual(response2.context['departments'].name, new_department2.name)