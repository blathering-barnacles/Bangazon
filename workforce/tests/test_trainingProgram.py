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
       # Check that the response is 200 OK.
        response = self.client.get(reverse('workforce:training'))

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.context['training_list']), 1)
        print('HERE HERHE HERE', new_program.name.encode())
        print('HERE HERHE HERE', response.content)

        
        test_me = b'\n<h2>View All Training Programs</h2>\n\n<ul>\n    \n    <li>Coding with dummy code</li>\n    \n</ul>\n\n<a href="/workforce/addtraining">Create New Training Program</a>'
        self.assertIn(response.content, test_me)





