from django.test import TestCase

class SmokeTest(TestCase):
    def test_bad_maths(slef):
        slef.assertEqual(1+1,3)