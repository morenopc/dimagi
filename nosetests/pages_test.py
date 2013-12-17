# -*- coding: UTF8 -*-
from random import randrange

from django.contrib.auth.models import User
from django.test import TestCase


class PagesTest(TestCase):
    """Get project pages test"""

    # fixtures = ['']

    def setUp(self):
        user = User.objects.create_user(
            'nosetest', 'nose@test.com', 'nosetest')
        self.client.login(username='nosetest', password='nosetest')

    def test_home(self):
        """Home page is working at '/' ?"""
        answer = self.client.get('/', follow=True)
        self.assertEqual(answer.status_code, 200,
            msg='GET {} {}'.format('/', answer.status_code))
