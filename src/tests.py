"""ローカルの単体テスト
"""

import unittest
from fibonacci import fib
from lambda_function import lambda_handler
from restutils import *

class TestFib(unittest.TestCase):
    def test_positive(self):
        testcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected  = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        self.assertEqual([fib(n) for n in testcases], expected)

    def test_negative(self):
        with self.assertRaises(ValueError):
            fib(0)
        with self.assertRaises(ValueError):
            fib(-1)
        with self.assertRaises(ValueError):
            fib("hoge")

class TestRequest(unittest.TestCase):
    def test_200(self):
        testcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected  = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        self.assertEqual(
            [lambda_handler(gen_request_event(n), None) for n in testcases],
            [gen_200(x) for x in expected])

    def test_400(self):
        self.assertEqual(lambda_handler(gen_request_event(0), None)['statusCode'], 400)
        self.assertEqual(lambda_handler(gen_request_event(-1), None)['statusCode'], 400)
        self.assertEqual(lambda_handler(gen_request_event("hoge"), None)['statusCode'], 400)




def test_all():
    unittest.main()

if __name__ == "__main__":
    test_all()
