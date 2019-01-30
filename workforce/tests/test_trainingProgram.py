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
        
        test_me = b'\n<h2>View All Training Programs</h2>\n\n<ul>\n    \n    <li>Coding with dummy code</li>\n    \n</ul>\n\n<a href="/workforce/addtraining">Create New Training Program</a>'
        
        self.assertIn(response.content, test_me)



TODO:
    # def test_get_program_form(self):
    #     response = self.client.get(reverse('workforce:addTraining'))
    #     # if this breaks check dev tools to get corrected input information
    #     print('*HERE*', response.content)
    #     print('TEST' )


    #     test_form = '<h3>Fill out the info for your form</h3>\n\n<form action="/workforce/addtraining/" method="post">\n    <input type="hidden" name="csrfmiddlewaretoken" value="1cpVFcND6bRls7Xci6Mfr942B8cojp7If6oxNo9yZf9rjLuhxCxyaV1WCxBod5p9">\n    <input type="text" name="trainName" />\n    <input type="date" name="trainStart" />\n    <input type="date" name="trainEnd" />\n    <input type="int" name="trainMax" />\n    <input type="submit" value="SAVE" />\n  </form>'

    #     self.assertIn(response.content, test_form)





