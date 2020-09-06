from unittest import TestCase
import coverage, flake8

class TryTesting(TestCase):
    def test_always_pass(self):
        self.assertTrue(True)
