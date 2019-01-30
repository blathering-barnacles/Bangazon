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

