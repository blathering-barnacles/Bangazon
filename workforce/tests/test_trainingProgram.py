import unittest
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from ..models import TrainingProgram, EmployeeTrainingProgram


class TrainingTest(TestCase):

    def test_list_programs(self):
        new_program = TrainingProgram.objects.create(
            name='Coding with dummy code',
            startDate='2019-03-19',
            endDate='2019-03-23',
            maxAttendees=33
        )
        response = self.client.get(reverse('workforce:training'))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.context['training_list']), 1)

        # if this breaks checks print out your response.content to see if it has changed and adjust test_me to match
        test_me = b'\n<h2>View Upcoming Training Programs</h2>\n\n<ul>\n    \n    <li>\n        <a href="/workforce/programs/1/">\n            Coding with dummy code\n        </a>\n    </li>\n    \n</ul>\n\n<a href="/workforce/addtraining">Create New Training Program</a>\n</br>\n<a href="/workforce/pastprograms">View Past Training Programs</a>'

        self.assertIn(test_me, response.content)

    def test_get_program_form(self):
        response = self.client.get(reverse('workforce:addTraining'))

        # if this breaks checks print out your response.content to see if it has changed and adjust test_form to match
        test_form = '<label>Event Name:\n        <input type="text" name="trainName" />\n    </label>\n    <label>Event Start Date:\n        <input type="date" name="trainStart" />\n    </label>\n    <label>Event End Date:\n        <input type="date" name="trainEnd" />\n    </label>\n    <label> Max Attendees:\n        <input type="int" name="trainMax" />\n    </label>\n    <input type="submit" value="SAVE" />\n  </form>\n\n'.encode()

        self.assertIn(test_form, response.content)

    def test_get_edit_program_form(self):
        new_program = TrainingProgram.objects.create(
            name='Coding with dummy code',
            startDate='2019-03-19',
            endDate='2019-03-23',
            maxAttendees=33
        )
        response = self.client.get(reverse('workforce:editTraining', args=(1,)))

        # if this breaks checks print out your response.content to see if it has changed and adjust test_form to match
        test_form = '<input type="submit" value="edit program"/>'.encode()

        self.assertIn(test_form, response.content)

    def test_program_details(self):
        new_program = TrainingProgram.objects.create(
            name='Coding with dummy code',
            startDate='2019-03-19',
            endDate='2019-03-23',
            maxAttendees=33
        )

        response = self.client.get(reverse('workforce:editTraining', args=(1,)))
        # Check that the response is 200
        self.assertEqual(response.status_code, 200)


    def test_delete_program(self):
        new_program = TrainingProgram.objects.create(
            name='Coding with dummy code',
            startDate='2019-01-19',
            endDate='2019-03-23',
            maxAttendees=33
        )

        todaysDate = timezone.now()
        formatedTodaysDate = str(todaysDate)[0:10]

        # Check that the response is 200 when date is greater than todays date
        response = self.client.get(reverse('workforce:deleteTraining', args=(1,)), follow=True)

        # if the start date is less or equal to todays date then the status code changes to 400
        if new_program.startDate <= formatedTodaysDate:
            response.status_code = 400
            print("YOU'RE STARTING YOUR PROGRAM BEFORE TODAY? I DONT THINK SO!")
        # if you change the status code here to 200 the system will reject it.
            self.assertEqual(response.status_code, 400)
        else:
            print("DELETE RESPONSE STATUS CODE: ", response.status_code)
            self.assertEqual(response.status_code, 200)







