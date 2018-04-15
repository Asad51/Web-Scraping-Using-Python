import requests
import bs4

session = requests.session()
req = session.post('http://localhost/foodsite/products.php', data=dict(category_id = '7', filter_products = 'Filter Products'))
soup = bs4.BeautifulSoup(req.content, 'lxml');
table = soup.find_all('table', {'class': 'information_table'})[0]
for tr in table.find_all('tr'):
    tds = tr.find_all('td')
    if len(tds) == 0:
        continue
    print(tds[0].get_text() + ' -> ' + tds[1].get_text())

res2 = session.get('http://localhost/foodsite/products.php')
soup2 = bs4.BeautifulSoup(res2.content, 'lxml')
table = soup2.find_all('table', {'class': 'information_table'})[0]
for tr in table.find_all('tr'):
    tds = tr.find_all('td')
    if len(tds) == 0:
        continue
    print(tds[0].get_text() + ' -> ' + tds[1].get_text())