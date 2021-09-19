def set_title(word):
    return word.title()

user_data = input('Введите слово или набор слов: ').split(' ')
result = list(map(lambda word: set_title(word), user_data))
print(' '.join(result))