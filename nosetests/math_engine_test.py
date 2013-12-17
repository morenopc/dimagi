# -*- coding: UTF8 -*-
from operator import mul

from random import randrange

from django.test import TestCase
from django.utils import simplejson


class PagesTest(TestCase):
    """Math engine app tests"""

    def test_math_engine_exists(self):
        """GET math engine exists?"""

        values = [randrange(-10, 10) for i in range(5)]
        answer = self.client.get('/math-engine/?values=%s' % values)
        self.assertEqual(answer.status_code, 200, msg=(
            'GET /math-engine/?values=%s %s' % (values, answer.status_code)))

    def test_math_engine_is_correct(self):
        """GET math engine response is correct?"""

        values = [randrange(-10, 10) for i in range(5)]
        answer = self.client.get('/math-engine/?values=%s' % values)
        # Load JSON
        content_dict = simplejson.loads(answer.content)
        # Sum
        self.assertEqual(content_dict['sum'], sum(values))
        # Product
        self.assertEqual(content_dict['product'], reduce(mul, values))
