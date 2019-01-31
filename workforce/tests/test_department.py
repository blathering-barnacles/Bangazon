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


        # TEST FOR TICKET 7 by ALFONSO MIRANDA
        responseDetail = self.client.get(reverse('workforce:departmentDetail', args=(1,)))


        print("RESPONSE CONTENT: ", responseDetail.content)
        print("RESPONSE CONTEXT: ", responseDetail.context['departments'])

        # Check that the response is 200 OK.
        self.assertEqual(responseDetail.status_code, 200)
        # Check that there is a property of name in fake new_department1 as there would be on a real new department.
        self.assertEqual(responseDetail.context['departments'].name, new_department1.name)

    def test_add_department(self):

        response = self.client.post(reverse('workforce:'))
#         Your test suite must verify that the content of the response has the required input fields.
# Your test suite must verify that when a POST operation is performed to the corresponding URL, then a successful response is received (i.e. status code must be 200)


    # def test_post_artist(self):

    #   response = self.client.post(reverse('history:artist_form'), {'name': 'Bill Board', 'birth_date': '10/31/67', 'biggest_hit': "So Blue Fer You"})

    #   # Getting 302 back because we have a success url and the view is redirecting
    #   self.assertEqual(response.status_code, 302)
