from bs4 import BeautifulSoup
import urllib.request


class Parser:
    
    raw_html = ''
    html = ''
    results = []
    
    def __init__(self, url, path):
        self.url = url
        self.path = path
    
    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')
    
    def parsing(self):
        news = self.html.find_all('div', class_='post-body')
        
        for item in news:
            self.results.append({
                'title': item.find('div', class_='title').get_text(strip=True),
                'desc': item.find('div', class_='the-excerpt').get_text(strip=True),
                'href': item.find('a', class_='read-more').get('href'),
            })
    def save(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            i = 1
            for item in self.results:
                f.write(f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсыдка: {item["href"]}\n\n****************************\n')
                i+=1
        
        
    def run(self):
        self.get_html()
        self.parsing()
        self.save()