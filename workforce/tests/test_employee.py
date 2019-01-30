import unittest
from django.test import TestCase
from django.urls import reverse
from ..models import Employee, Department

class EmployeeTest(TestCase):

    def test_list_employee(self):
        """adds new employee and department to temp database and confirms accurate response
        code, addition of employee to table and confirms that accurate first name, last name and
        department are being returned """
        new_employee = Employee.objects.create(
            firstName="Richard",
            lastName="Lancaster",
            startDate="1998-08-17",
            isSupervisor="1",
            department_id="1"
        )

        new_department = Department.objects.create(
            name="Accounting",
            budget=100000
        )

        response = self.client.get(reverse('workforce:employeeList'))

        self.assertEqual(response.status_code, 200)  # Check that the response is 200 OK.
        self.assertEqual(len(response.context['all_employees']), 1)
        self.assertIn(new_employee.firstName.encode(), response.content)
        self.assertIn(new_employee.lastName.encode(), response.content)
        self.assertIn(new_department.name.encode(), response.content)

    # def test_get_artist_form(self):

    #   response = self.client.get(reverse('history:artist_form'))

    #   self.assertIn(
    #       '<input type="text" name="name" maxlength="100" required id="id_name">'.encode(), response.content)

    # def test_post_artist(self):

    #   response = self.client.post(reverse('history:artist_form'), {'name': 'Bill Board', 'birth_date': '10/31/67', 'biggest_hit': "So Blue Fer You"})

    #   # Getting 302 back because we have a success url and the view is redirecting
    #   self.assertEqual(response.status_code, 302)

    # def test_get_artist_detail(self):
    #   new_artist = Artist.objects.create(
    #       name="Suzy Saxophone",
    #       birth_date="12/25/58",
    #       biggest_hit="Honk Honk Squeak"
    #   )

    #   response = self.client.get(reverse('history:artist_detail', args=(1,)))
    #   self.assertEqual(response.context["artist_detail"].name, new_artist.name)

