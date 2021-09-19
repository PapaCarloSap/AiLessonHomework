import unittest
import HomeWork7.project2 as prj_2


class TestProjects(unittest.TestCase):

    # Project_2
    def test_add_coat_add_suit(self):
        coat = prj_2.Coat(1)
        suit = prj_2.Suit(1)
        self.assertEqual('4.47', f'{(suit+coat).area:.3}')



if __name__ == '__main__':
    unittest.main()