import unittest
from django.test import TestCase
from django.urls import reverse
from ..models import Department, Employee

class DepartmentTest(TestCase):

    # =================================================================
    # Dillon's Test for ticket 5
    def test_list_departments(self):
        new_department1 = Department.objects.create(
            name="Coding Crew",
            budget="55000"
        )

        # print(new_department1)

        # Issue a GET request. "client" is a dummy web browser
        # 'reverse' is used to generate a URL for a given view. The main advantage is that you do not hard code routes in your code.
        # Below our pretend client is making a virtual HTTP request to GET the departments
        response = self.client.get(reverse('workforce:departmentList'))
        # print(response.content)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 1 department.
        # Response.context is the context variable passed to the template by the view. This is incredibly useful for testing, because it allows us to confirm that our template is getting all the data it needs.
        self.assertEqual(len(response.context['latest_dept_list']), 1)

        # .encode converts from unicode to utf-8
        # example:
        # If the string is: python!
        # The encoded version is: b'pyth\xc3\xb6n!'
        self.assertIn(new_department1.name.encode(), response.content)
    # ==================================================================

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
        responseDetail = self.client.get(reverse('workforce:departmentDetail', args=(1,)))


        print("RESPONSE CONTENT: ", responseDetail.content)
        print("RESPONSE CONTEXT: ", responseDetail.context['departments'])

        # Check that the response is 200 OK.
        self.assertEqual(responseDetail.status_code, 200)
        self.assertEqual(responseDetail.context['departments'].name, new_department1.name)
