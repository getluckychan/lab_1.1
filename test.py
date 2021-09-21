import unittest
from pay import Pay

class TestPay(unittest.TestCase):
    def setUp(self):
        self.pay = Pay(first=1, second=1, days=1)

    def test_summa(self):
        self.assertEqual(self.pay.summa(), 1.0)


if __name__ == '__main__':
    unittest.main()
