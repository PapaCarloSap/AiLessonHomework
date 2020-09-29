import unittest
import piece as target


class TestProjects(unittest.TestCase):

    def test_piece_number(self):
        piece = target.Piece(5)
        self.assertEqual(5, piece.number)

    def test_pieces_init(self):
        pieces = target.Pieces()
        self.assertEqual(90, pieces.count)
        # for item in range(1, 90):
        #     self.assertEqual(item, pieces.__piece_list[item].number, f'Свалилось на {item}')

    def test_pieces_get_random_piece(self):
        pieces = target.Pieces()
        result = list()
        for item in range(90):
            result.append(pieces.get_random_piece().number)
        self.assertEqual(90, len(set(sorted(result))))
        self.assertEqual(None, pieces.get_random_piece())

if __name__ == '__main__':
    unittest.main()