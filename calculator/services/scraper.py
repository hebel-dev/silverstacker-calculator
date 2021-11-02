from os import replace
from re import findall
from bs4 import BeautifulSoup
import requests
import unicodedata


# html_text = requests.get('https://pl.ucoin.net/coin/ajman-1-riyal-1969/?tid=87655')
# soup =BeautifulSoup (html_text.text, features="lxml")

# def cleanHTML(data):
#     soup = BeautifulSoup(data)
#     for text in soup.find_all

url = 'https://pl.ucoin.net/catalog/?year=1865-2022&composition=189'
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}

webpage = requests.get(url,headers=headers)
soup = BeautifulSoup(webpage.content, 'lxml')





def scrap_data():
    for table_coin in soup.find_all('table', class_= 'coin'):
       
        print(table_coin.div.text)
        name = table_coin.find('a', class_='value').text
        
        print(name)
        year_list=name.split(',')
        year_list = year_list[1].split('-')
        # if year list len remove if coś tam metoda do wyjęcia z listy 
        print('year list', year_list) 
        # print(table_coin)
        country_link = table_coin.find('a', class_='value')['href'] 
        print(country_link)
        country_name_dash = country_link.split('/')[2]
        country_name = country_name_dash.split('-')[0]
        print(country_name)
        print()
    return

scraped_data = scrap_data()


def scrap_urls():
    a  = soup.find('div', class_='pages')
    c = []
    for b in  a.find_all('a', href=True):   
        c.append(b.text)
    
    return c
scraped_urls = scrap_urls()
print(scraped_urls)



# class CoinScraper:
#     def __init__(self):






# class Scraper:
#     base_url = 'https://pl.ucoin.net/catalog/?country=england&composition=189'
#     def __init__(self):
#         ...


#     def run(self):
#         # 1. zrób mi wszystkie urle
#         self.get_all_urls()
#         # 2. dla kązdego urla pobnierz html
#         # 3. dla każdego coina na hmtl pobierz
#         # 4. dla każdej monety spradz czy dane są sensonwe
#         # 5. jak tak to zapoisz do bazy
#         pass

#     def get_all_urls(self):
#         max_page_niumber = self.scrap_max_page_number()
#         urls = []
#         for i in range(max_page_niumber):
#             urls.append(f'{self.base_url}&page={i}')
#         print(urls)


# scrpaer = Scraper()
# scrpaer.run()
