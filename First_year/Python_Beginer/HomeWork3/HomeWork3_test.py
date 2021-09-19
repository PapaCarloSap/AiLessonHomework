import unittest

# from HomeWork3.Project_1 import custom_div
# from HomeWork3.Project_1 import convert_to_divisible_and_divider
from Project_3 import get_max_sum
from Project_4 import get_exponentiation

# class TestProject_1(unittest.TestCase):
#     """
#     Test for Project_1
#     """
#     def test_custom_div(self):
#         self.assertEqual(0.5, custom_div(5,10))

#     def test_convert_to_divisible_and_divider(self):
#         self.assertEqual((1,-2), tuple(convert_to_divisible_and_divider('1', '-2')))
#         self.assertEqual((1,None), tuple(convert_to_divisible_and_divider('1', '0')))
#         self.assertEqual((None,2), tuple(convert_to_divisible_and_divider('sss', '2')))
#         self.assertEqual((10,None), tuple(convert_to_divisible_and_divider('10', 'sss')))

#     def test_main(self):
#         divisible, divider = convert_to_divisible_and_divider('10', '-2')
#         self.assertEqual(-5, custom_div(divisible, divider))

class TestProject_3(unittest.TestCase):
    """
    Test for Project_3
    """
    def test_get_max_sum(self):
        self.assertEqual(5, get_max_sum(3,2,1))
        self.assertEqual(-3, get_max_sum(-1,-2,-3))
        self.assertEqual(10, get_max_sum(0,-10, 10))

class TestProject_4(unittest.TestCase):
    """
    Test for Project_4
    """
    def test_get_max_sum(self):
        self.assertEqual(8, get_exponentiation(2,3))
        self.assertEqual(1, get_exponentiation(2,0))
        self.assertEqual(2, get_exponentiation(2,1))
        self.assertEqual(10**(-3), get_exponentiation(10,-3))


if __name__ == '__main__':
    unittest.main()