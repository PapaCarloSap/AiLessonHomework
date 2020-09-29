import unittest
import player as target
from card import Card 
from platform import node
from piece import Pieces


class TestProjects(unittest.TestCase):

    def test_user_name(self):
        pc = target.PcPlayer(Card())        
        user = target.UserPlayer('Test user', Card())        
        self.assertEqual('Test user', user.name)
        self.assertEqual(node(), pc.name)

    def test_get_display_card(self):
        pc = target.PcPlayer(Card())      
        self.assertTrue(len(pc.get_display_card())>110)

    def test_apply_piece(self):
        pieces = Pieces()
        pc = target.PcPlayer(Card())      
        while pieces.count !=0:
            pc.apply_piece(pieces.get_random_piece())
        self.assertTrue(pc.on_card_all_cross)


if __name__ == '__main__':
    unittest.main()