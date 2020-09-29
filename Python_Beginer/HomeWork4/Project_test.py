import unittest

import Project_1
import Project_2
import Project_3
import Project_4
import Project_5
import Project_6
import Project_7


class TestProjects(unittest.TestCase):

    # Project_1
    def test_get_salary(self):
        self.assertEqual(20, Project_1.get_salary(8, 2, 4))
        
    # Project_2
    def test_get_max_list(self):
        self.assertEqual([12, 44, 4, 10, 78, 123], Project_2.get_max_list([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]))

    # Project_3
    def test_find_multiple(self):
        self.assertEqual([2,3,4,6], Project_3.find_multiple(range(1,7), 2, 3))

    # Project_4
    def test_get_list(self):
        self.assertEqual([2], Project_4.get_list([1,1,2,3,3]))
        self.assertEqual([23, 1, 3, 10, 4, 11], Project_4.get_list())
    # Project_5
    def test_get_sum_items(self):
        self.assertEqual(8, Project_5.get_list(range(1,5)))
        self.assertEqual(8, Project_5.get_list(range(2,5)))

    # Project_6
    def test_create_infinite_list(self):
        self.assertEqual([2, 3, 4, 5, 6], list(Project_6.generate_infinite_list(2, 6)))
    
    def test_create_cycle_list(self):
        self.assertEqual(['first', 'second', 'first', 'second'], list(Project_6.generate_cycle_list(['first', 'second'], 2)))

    # Project_7
    def test_fact(self):
        self.assertEqual([1,2,6,24], list(Project_7.fact(4)))

if __name__ == '__main__':
    unittest.main()
