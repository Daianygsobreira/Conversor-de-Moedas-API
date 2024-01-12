import unittest
import json
from convertapp import app

class TestCurrencyConversion(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)

    def test_successful_conversion(self):
        response = self.tester.get('/convert?from=USD&to=BRL&amount=100')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)
        self.assertIn('converted_amount', data)
        self.assertIn('from', data)
        self.assertIn('to', data)
        self.assertEqual(data['from'], 'USD')
        self.assertEqual(data['to'], 'BRL')


    def test_invalid_amount(self):
        response = self.tester.get('/convert?from=USD&to=BRL&amount=abc')
        self.assertEqual(response.status_code, 400)

    def test_unsupported_currency(self):
        response = self.tester.get('/convert?from=XYZ&to=BRL&amount=100')
        self.assertEqual(response.status_code, 400)

#

if __name__ == "__main__":
    unittest.main()
