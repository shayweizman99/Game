from unittest import TestCase, mock
from Unittest import Calculator

class Test_calc(TestCase):
    @mock.patch("Unittest.Calculator.Calculator.sum_numbers" , return_value=15)

    def test_sum_numbers(self, mock_sum_numbers):
        calc =Calculator(4, 4)
        print(calc.sum_numbers())
        self.assertEqual(calc.sum_numbers() , 9)



