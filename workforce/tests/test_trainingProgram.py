import unittest
from django.test import TestCase
from django.urls import reverse
from ..models import TrainingProgram


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
        test_form = '<label>Event Name:\n        <input type="text" name="trainName" />\n    </label>\n    <label>Event Start Date:\n        <input type="date" name="trainStart" />\n    </label>\n    <label>Event End Date:\n        <input type="date" name="trainEnd" />\n    </label>\n    <label> Max Attendees:\n        <input type="int" name="trainMax" />\n    </label>\n    <input type="submit" value="SAVE" />\n</form>'.encode()

        self.assertIn(test_form, response.content)





