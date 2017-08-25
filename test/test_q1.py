from unittest import TestCase
from questions.q1 import get_max


class TestQ1(TestCase):
    def test_q1(self):
        x1 = [1, 2, 3, 4, 5]
        y1 = 5
        self.assertEqual(get_max(x1), y1)
        x2 = [214, 33, -192, 391, 10, 398, 9877, 1911, 90, 4, -55, 50]
        y2 = 9877
        self.assertEqual(get_max(x2), y2)
        x3 = []
        self.assertTrue(get_max(x3) is None)