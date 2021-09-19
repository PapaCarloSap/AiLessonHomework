from game import Game

user_wonts_play_game = True
users = input('Введите имена играков, через запятую: ').split(',')
while user_wonts_play_game:
    game = Game(users)
    game.play()
    while True:
        user_data = input('Игра закончена, хотели бы съиграть еще раз (y/n): ')
        if user_data.lower() == 'y':
            user_wonts_play_game = True
            break
        elif user_data.lower() == 'n':
            user_wonts_play_game = False
            break
        else:
            print('Не верно введены данные')