from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User

class ListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 employees for pagination tests
        number_of_employees = 13

        for employees_id in range(number_of_employees):
            User.objects.create(
                first_name=f'Christian {employees_id}',
                last_name=f'Surname {employees_id}',
            )