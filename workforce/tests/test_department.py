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

        # Issue a GET request. "client" is a dummy web browser
        # 'reverse' is used to generate a URL for a given view. The main advantage is that you do not hard code routes in your code.
        # Below our pretend client is making a virtual HTTP request to GET the departments
        response = self.client.get(reverse('workforce:departmentList'))

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

        # Check that the response is 200 OK.
        self.assertEqual(responseDetail.status_code, 200)
        # Check that there is a property of name in fake new_department1 as there would be on a real new department.
        self.assertEqual(responseDetail.context['departments'].name, new_department1.name)

    def test_add_department(self):

        post_response = self.client.post(reverse('workforce:addDepartment'), {'department_name': 'Finance', 'department_budget': 2000})

        self.assertEqual(post_response.status_code, 302)

        form_response = self.client.get(reverse('workforce:departmentForm'))
        form_content = '<label for="dept_name">Department Name</label>\n    <input type="text" name="department_name" id="dept_name">\n    <label for="dept_budget">Department Budget</label>\n    <input type="text" name="department_budget" id="dept_budget">\n\n    <input type="submit" value="Save Department">'

        self.assertIn(form_content.encode(), form_response.content)