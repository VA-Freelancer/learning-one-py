#parsing / pip https://pypi.org/

from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://hi-tech.news/')
html = req.read()
# print(html)
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
news = soup.find_all('div', class_='post-body')
# print(news)

results = []

for item in news:
    results.append({
        'title': item.find('div', class_='title').get_text(strip=True),
        'desc': item.find('div', class_='the-excerpt').get_text(strip=True),
        'href': item.find('a', class_='read-more').get('href'),
    })


print(results)

f = open('news.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсыдка: {item["href"]}\n\n****************************\n')
    i+=1
f.close()