user_data = input('Введите строку и нескольких слов: ')
user_words = user_data.split(' ')
for index in range(len(user_words)):
    user_word = user_words[index]
    if(len(user_word)>10):
        user_word = user_word[:10]
    print(f'{index+1}. {user_word}')