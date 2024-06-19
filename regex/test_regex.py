from regex import get_struct
import unittest


class test_regex(unittest.TestCase):
    def test_get_struct(self):
        self.assertIsNotNone(get_struct('struct State {'))
        
    def test_not_struct(self):
        self.assertIsNone(get_struct('struct State }'))

    def test_always_pass(self):
        self.assertTrue(True)