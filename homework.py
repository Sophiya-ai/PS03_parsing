import requests as req
from bs4 import BeautifulSoup as BS
from googletrans import Translator

# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = 'https://randomword.com/'
    try:
        res = req.get(url)
        soup = BS(res.content, 'html.parser')

        # Получаем слово. text.strip удаляет все пробелы из результата
        e_word = soup.find('div', id='random_word').text.strip()
        # Получаем описание слова
        w_def = soup.find('div', id='random_word_definition').text.strip()

        # Чтобы программа возвращала словарь
        return {
            "english_word": e_word,
            "english_word_definition": w_def
        }
    except:
        print('Error!')

#функция перевода
def translation(text):
    trans = Translator()
    return trans.translate(text, dest='ru')

# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру! \n")
    while True:
        word_dict = get_english_words()
        word = translation(word_dict.get("english_word"))
        word_definition = translation(word_dict.get("english_word_definition"))

        # Начинаем игру
        print(f"Значение слова - {word_definition.text}")
        user = input("Что это за слово? ")
        if user == word.text:
            print("Все верно!")
        else:
            print(f"\nОтвет неверный, было загадано это слово - {word.text}")

        # Создаём возможность закончить игру
        play_again = input("\nХотите сыграть еще раз? y/n ")
        if play_again != "y":
            print("Спасибо за игру!")
            break


word_game()


