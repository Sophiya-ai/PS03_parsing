import requests as req
from bs4 import BeautifulSoup as BS

#Создаём функцию, которая будет получать информацию
def get_english_words():
    url = 'https://randomword.com/'
    try:
        res = req.get(url)
        #print(res.text)
        soup = BS(res.content,'html.parser')

        # Получаем слово. text.strip удаляет все пробелы из результата
        e_word = soup.find('div', id='random_word').text.strip()
        # Получаем описание слова
        w_def = soup.find('div', id='random_word_definition').text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_word" : e_word,
            "english_word_definition" : w_def
        }
    except:
        print('Error!')

# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_word")
        word_definition = word_dict.get("english_word_definition")

        # Начинаем игру
        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ")
        if user == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again != "y":
            print("Спасибо за игру!")
            break



word_game()

    
