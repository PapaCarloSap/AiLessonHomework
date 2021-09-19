from piece import Pieces


class Arbiter(object):
    def __init__(self, players):
        self.__pieces = Pieces()
        self.__piece = None
        self.__players = players

    @property
    def current_piece(self):
        return self.__piece

    @property
    def piece_len(self):
        return self.__pieces.count

    def get_new_piece(self):
        self.__piece = self.__pieces.get_random_piece()

    def send_piece_players(self):
        for player in self.__players:
            player.apply_piece(self.__piece)

    def check_winner_players(self):
        losers = list()
        winner = list()
        for player in self.__players:
            if player.on_card_all_cross:
                winner.append(player)
                continue
            if player.is_mistake:
                losers.append(player)
        for player in losers:
            self.__players.remove(player)
        if len(self.__players) == 1:
            winner.append(self.__players[0])
        return winner, losers

    # def check_winner_players(self):
    #     losers = list()
    #     winner = None
    #     for player in self.__players:
    #         if player.on_card_all_cross:
    #             winner = player
    #             break
    #         if player.is_mistake:
    #             losers.append(player)
    #     for player in losers:
    #         self.__players.remove(player)
    #     if len(self.__players) == 1:
    #         winner = self.__players[0]
    #     return winner, losers
