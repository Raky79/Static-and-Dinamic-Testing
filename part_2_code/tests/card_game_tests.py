import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self): 
        self.ace = Card("Ace",11)
        self.king = Card("King",10)
        self.queen = Card("Queen", 10)
        self.jack = Card("Jack", 10)
        self.card_game = CardGame(0, [])

    
    def test_check_for_ace__is_ace(self):
        self.card_game.check_for_ace(self.ace) 
        self.assertEqual(True, self.card_game.check_for_ace(self.ace))
    
    def test_check_for_ace__is_Not_ace(self):  
        self.card_game.check_for_ace(self.king) 
        self.assertEqual(False, self.card_game.check_for_ace(self.king))
    
    def test_highest_card(self):
        card1 = self.queen
        card2 = self.ace
        self.card_game.highest_card(card1, card2)
        self.assertEqual(card2, self.card_game.highest_card(self.queen,self.ace))
    
    def test_cards_total(self):
        card1 = self.queen
        card2 = self.ace
        card3 = self.jack
        card4 = self.king
        self.card_game.cards_total(card1)
        self.card_game.cards_total(card2)
        self.card_game.cards_total(card3)
        self.card_game.cards_total(card4)  
        self.assertEqual("You have a total of 0", self.card_game.cards_total(card1))
        

    # card1 = self.queen
    #     card2 = self.ace
    #     card3 = self.jack
    #     card4 = self.king
    #     cards = card1+card2+card3+card4
    #     self.assertEqual("You have a total of 41", self.card_game.cards_total(cards)) 
     
       
    

        


   