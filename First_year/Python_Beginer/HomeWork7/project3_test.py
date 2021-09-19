import unittest
import HomeWork7.project3 as prj


class TestProjects(unittest.TestCase):

    def test_add_cell(self):
        cell1 = prj.Cell(3)
        cell2 = prj.Cell(1)
        self.assertEqual(4, (cell1+cell2)._point)

    def test_sub_cell(self):
        cell1 = prj.Cell(3)
        cell2 = prj.Cell(1)
        self.assertEqual(2, (cell1-cell2)._point)

    def test_sub_cell_message(self):
        cell1 = prj.Cell(3)
        cell2 = prj.Cell(1)
        self.assertEqual('Не возможно выполнить вычитание ячеек из клетки', cell2-cell1)

    def test_mul_cell(self):
        cell1 = prj.Cell(3)
        cell2 = prj.Cell(2)
        self.assertEqual(6, (cell1*cell2)._point)

    def test_div_cell_1(self):
        cell1 = prj.Cell(9)
        cell2 = prj.Cell(8)
        self.assertEqual(2, (cell1/cell2)._point)

    def test_div_cell_2(self):
        cell1 = prj.Cell(9)
        cell2 = prj.Cell(8)
        self.assertEqual(1, (cell2/cell1)._point)

    def test_make_order(self):
        cell = prj.Cell(8)
        self.assertEqual('***\n***\n**', cell.make_order(3))



if __name__ == '__main__':
    unittest.main()