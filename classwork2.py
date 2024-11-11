import requests as req
from bs4 import BeautifulSoup as BS

#Создаём функцию, которая будет получать информацию
def get_english_words():
    url = 'https://randomword.com/'
    try:
        res = req.get(url)
        print(res.text)
        soup = BS(res.content,'html.parser')

        # Получаем слово. text.strip удаляет все пробелы из результата
        e_words = soup.find_all('div', id='random_word')
        # Получаем описание слова
        w_def = soup.find_all('div', id='random_word_definition')
        # Чтобы программа возвращала словарь
        return {
            "english_words" : e_words,
            "english_word_definition" : w_def
        }
    except:
        print('Error!')

    
