# -*- coding: UTF8 -*-
from random import randrange

from django.test import TestCase


class PagesTest(TestCase):
    """Math engine app tests"""

    def test_math_engine_GET(self):
        """GET math engine response is correct?"""

        values = [randrange(-10, 10) for i in range(5)]
        answer = self.client.get('/math-engine/?values=%s' % values)
        self.assertEqual(answer.status_code, 200, msg=(
            'GET /math-engine/?values=%s %s' % (values, answer.status_code)))
