from unittest import TestCase
from questions.q2 import get_most_common_char


class TestQ2(TestCase):
    def test_q2(self):
        x1 = "aaa aa aaa bbb bb c d"
        y1 = "a"
        self.assertEqual(get_most_common_char(x1), y1)
        x2 = "Aaa Aa AAA bbb bb c d"
        y2 = "a"
        self.assertEqual(get_most_common_char(x2), y2)
