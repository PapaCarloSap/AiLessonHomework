from platform import node
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name, card):
        self.__name = name
        self._card = card
        self._is_mistake = False
        self._on_card_all_cross = False

    @property
    def name(self):
        return self.__name

    @property
    def is_mistake(self):
        return self._is_mistake
        
    @property
    def on_card_all_cross(self):
        return self._on_card_all_cross

    def get_display_card(self):
        return f'========== {self.__name} ===========\n{self._card}------------------------------------\n\n' 

    @abstractmethod
    def apply_piece(self, piece):
        pass
        

class UserPlayer(Player):
    def __init__(self, name, card):
        super().__init__(name, card)

    def apply_piece(self, piece):
        need_cross = self.__ask_user_need_cross_number(piece.number)
        if need_cross and self._card.cross_piece(piece):
            self._on_card_all_cross = self._card.is_all_cross()
            return
        if not self._card.contained_piece(piece) and not need_cross:
            return
        self._is_mistake = True
        
    def __ask_user_need_cross_number(self, number):
        while True:
            user_data = input(f'Зачеркунуть цифру: {number} (y/n) ')
            if user_data.lower() == 'y':
                return True
            elif user_data.lower() == 'n':
                return False
            else:
                print('Не верно введены данные')


class PcPlayer(Player):
    def __init__(self, card, name = node()):
        super().__init__(name, card)

    def apply_piece(self, piece):
        if self._card.cross_piece(piece):
            self._on_card_all_cross = self._card.is_all_cross()