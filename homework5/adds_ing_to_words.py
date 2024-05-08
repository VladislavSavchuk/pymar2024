"""Adds 'ing' to words.
The program adds 'ing' to words
"""


def add_ing_to_words_1():
    """This function adds 'ing' to the words in the string"""
    # Создаем строку со словами
    line = "read, sing, meet, copy, study, buy"

    # Разбиваем строку по символу ',' при помощи метода split()
    words = line.split(',')

    # Инициализируем переменную
    new_words = ""

    # Проходим перебором по каждому слову в строке
    for word in words:
        # Берем каждое слово и добавляем "ing"
        new_words += word + "ing"

    print(f"Строка  с добавлением 'ing' к словам: {new_words}")
    print()


add_ing_to_words_1()


def add_ing_to_words_2(sentence):
    """This function searches through the words and joins words using join()"""
    # Разбиваем строку на слова при помощи метода split()
    words = sentence.split()

    # Создаем пустой список для хранения слов с 'ing'
    ing_words = []

    # Перебираем каждое слово в списке words
    for word in words:
        # Добавляем результат в список ing_words при помощи метода append()
        ing_words.append(add_ing(word))

    # Объединяем слова обратно в строку с помощью метода join() через пробел.
    return ' '.join(ing_words)


def add_ing(word):
    """This function checks and adds 'ing' to the words in the string"""
    # Проверяем, что слово состоит хотя бы из трех букв
    if len(word) >= 3:
        # Если слово заканчивается на 'ie', заменяем 'ie' на 'ying'
        if word.endswith('ie'):
            return word[:-2] + 'ying'
        # Если слово заканчивается на 'e', удаляем 'e' и добавляем 'ing'
        elif word[-1] == 'e':
            return word[:-1] + 'ing'
        # В остальных случаях просто добавляем 'ing' в конец слова
        else:
            return word + 'ing'
    else:
        return word


# Создаем строку со словами
MY_STRING = "study spin prefer die travel see"

# Выводим результат
print("Строка слов с окончанием на 'ing':", add_ing_to_words_2(MY_STRING))
