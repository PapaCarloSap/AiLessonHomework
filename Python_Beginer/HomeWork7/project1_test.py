import unittest
import HomeWork7.project1 as prj_1


class TestProjects(unittest.TestCase):

    # Project_1
    def test_add_2x3(self):
        matrix1 = prj_1.Matrix([[1, 2], [3, 4]])
        matrix2 = prj_1.Matrix([[-1, -2], [-3, -4]])
        self.assertEqual(str([[0, 0], [0, 0]]), str((matrix1 + matrix2)._source))

    def test_add_0x0(self):
        matrix1 = prj_1.Matrix([[0]])
        matrix2 = prj_1.Matrix([[0]])
        matrix3 = matrix1 + matrix2
        self.assertEqual([[0]], matrix3._source)

    def test_add_2x2_add_3x3(self):
        matrix1 = prj_1.Matrix([[1, 2], [3, 4]])
        matrix2 = prj_1.Matrix([[1, -1, -2], [2, -3, -4], [3, 4, 5] ])
        self.assertEqual(str([[2, 1, -2], [5, 1, -4], [3, 4, 5]]), str((matrix1 + matrix2)._source))


if __name__ == '__main__':
    unittest.main()
