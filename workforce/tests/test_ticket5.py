import unittest
from django.test import TestCase
from django.urls import reverse
from ..models import Department


class DepartmentDetailTest(TestCase):

    def test_list_departments(self):
        new_department1 = Department.objects.create(
            name="Fuck we need a hugh",
            budget="4000")


        new_department2 = Department.objects.create(
            name="Yes we do",
            budget="5000")

        # print(new_department)

        # Issue a GET request. "client" is a dummy web browser
        # 'reverse' is used to generate a URL for a given view. The main advantage is that you do not hard code routes in your code.
        response = self.client.get(reverse('workforce:departmentList', args=(1,)))
        print(response.content)

        self.assertEqual(response.status_code, 200)