from bs4 import BeautifulSoup as BS
import requests as req

url = 'http://quotes.toscrape.com/'
response = req.get(url)
html = response.text
soup = BS(html,'html.parser')

links = soup.find_all('a') #внутри тег а, тк ссылки нам нужны
for link in links:
    print(link.get('href'))#у каждого тега есть параметры у а - это href, так мы выведем только ссылки

#выберем цитаты
text1 = soup.find('span',class_='text')#выбрали первую цитату
#print(text1)
text = soup.find_all('span',class_='text')
#print(text)
author = soup.find_all('small', class_ = 'author')
print(author)
for i in range(len(text)):
    print(f"Цитата номер {i+1}")
    print(text[i].text)
    print(f"Автор: {author[i].text}\n")


