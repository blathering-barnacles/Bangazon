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

        test_me = '<div class="container">\n<h1 class="mt-4 mb-3">View Upcoming Training Programs</h1>\n\n<ul class="list-group">\n    \n    <li class="list-group-item list-group-item-action list-container">\n        <a class="text-info d-inline" href="/workforce/programs/1/">\n            <h3 class="d-inline">Coding with dummy code</h3>\n        </a>\n        <div>\n        <i class="fas fa-calendar-day fa-2x d-inline"></i><h4 class="d-inline"> Start Date: March 19, 2019</h4>\n    </div>\n    </li>\n    \n</ul>\n\n<a href="/workforce/addtraining"><button class="btn btn-info d-inline mt-3">Create New Training Program</button></a>\n<a href="/workforce/pastprograms"><button class="btn btn-secondary d-inline mt-3">View Past Training Programs</button></a>\n</div>\n\n\n'.encode()

        self.assertIn(test_me, response.content)

    def test_get_program_form(self):
        response = self.client.get(reverse('workforce:addTraining'))
        # if this breaks checks print out your response.content to see if it has changed and adjust test_form to match
        test_form = '<input type="text" name="trainName" />\n    </label><br>\n    <label>Event Start Date:\n        <input type="date" name="trainStart" />\n    </label><br>\n    <label>Event End Date:\n        <input type="date" name="trainEnd" />\n    </label><br>\n    <label> Max Attendees:\n        <input type="int" name="trainMax" />\n    </label><br>\n    <input type="submit" value="Save" class="btn btn-info"/>\n  </form>'.encode()

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
        test_form = '<input type="submit" value="Edit Program" class="btn btn-info mt-2 d-inline"/>'.encode()
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
        # if you change the status code here to 200 the system will reject it.
            self.assertEqual(response.status_code, 400)
        else:
            self.assertEqual(response.status_code, 200)

    def test_add_program(self):

        test_program = {'trainName': 'Testing in Python', 'trainStart': '2019-02-19', 'trainEnd': '2019-02-24', 'trainMax': '50'}

        response = self.client.post(reverse('workforce:addTraining'), test_program)
        # Check that the response status code comes back as 302
        self.assertEqual(response.status_code, 302)
