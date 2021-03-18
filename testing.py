import unittest
import main_for_test

class TestMain(unittest.TestCase):
    def test_fn1(self):
        test_param = 10
        result = main_for_test.add_five(test_param)
        self.assertEqual(result, 15)

    def test_fn2(self):
        test_param = 'num'
        result = main_for_test.add_five(test_param)
        # self.assertEqual(result, 'Can only accept digits.')
        self.assertTrue(isinstance(result, TypeError))
        self.assertIsInstance(result, TypeError)

    def test_fn3(self):
        test_param = None
        result = main_for_test.add_five(test_param)
        self.assertEqual(result, 'Please enter a number.')

    def test_fn4(self):
        test_param = ''
        result = main_for_test.add_five(test_param)
        self.assertEqual(result, 'Please enter a number.')

    def test_fn5(self):
        test_param = 0
        result = main_for_test.add_five(test_param)
        self.assertEqual(result, 5)
    
    def test_fn6(self):
        test_param = -5
        result = main_for_test.add_five(test_param)
        self.assertEqual(result, 0)

if(__name__ == '__main__'):
    unittest.main()
