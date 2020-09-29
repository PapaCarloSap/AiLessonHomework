from arbiter import Arbiter
from player import UserPlayer, PcPlayer
from arbiter import Arbiter
from card import Card


class Game(object):
    def __init__(self, user_names):
        #self.__players = [PcPlayer(Card(), 'ddd'), PcPlayer(Card()),PcPlayer(Card(), 'player 1'), PcPlayer(Card(), 'player 2')]
        self.__players = [PcPlayer(Card())]
        for user_name in user_names:
            self.__players.append(UserPlayer(user_name, Card()))
        self.__arbiter = Arbiter(self.__players)

    def play(self):
        while True:
            self.show_players_card()
            self.__arbiter.get_new_piece()
            self.show_current_piece()
            self.__arbiter.send_piece_players()
            winners, losers = self.__arbiter.check_winner_players()
            if len(winners)>0:
                for winner in winners:
                    print(f'Выйграл: {winner.name}')
                break
            else:
                if len(losers) != 0:
                    for loser in losers:
                        print(f'Проиграл: {loser.name}')
            
    def show_players_card(self):
        for player in self.__players:
            print(player.get_display_card())
            
    def show_current_piece(self):
        print(f'Осталось боченков: {self.__arbiter.piece_len} Текущий номер: {self.__arbiter.current_piece}')