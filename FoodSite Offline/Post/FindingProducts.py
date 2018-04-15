import requests
import bs4

page = requests.post('http://localhost/foodsite/products.php', data=dict(search = 'Search',search_string = 'rice'))
soup = bs4.BeautifulSoup(page.content, 'lxml')
table = soup.find_all('table', {'class':'information_table'})
for tr in table.find_all('tr'):
    tds = tr.find_all('td')
    if len(tds) == 0:
        continue
    print(tds[0].get_text() + ' -> ' + tds[1].get_text())