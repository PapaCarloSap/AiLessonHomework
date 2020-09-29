import unittest
import card as target


class TestProjects(unittest.TestCase):

    def test_card_number(self):
        card = target.Card()        
        a = len(card._Card__repo)
        self.assertEqual(3, len(card._Card__repo))
        self.assertEqual(5, len(card._Card__repo[0]))
        self.assertEqual(5, len(card._Card__repo[1]))
        self.assertEqual(5, len(card._Card__repo[2]))
        self.assertEqual(4, len([card._Card__repo[0][i-1] for i in range(1, 5) if card._Card__repo[0][i]>card._Card__repo[0][i-i]]))

    def test_card_display(self):
        card = target.Card()        
        a = len(card._Card__repo)
        print(card)
        self.assertEqual(111, len(str(card)))
        

if __name__ == '__main__':
    unittest.main()