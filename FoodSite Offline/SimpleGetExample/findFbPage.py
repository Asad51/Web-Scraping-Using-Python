import requests
import bs4

req = requests.get('http://localhost/foodsite/announcements.php')
soup = bs4.BeautifulSoup(req.content, 'lxml')
table = soup.find_all('table', {'class': 'information_table'})[0]
for tr in table.find_all('tr'):
    tds = tr.find_all('td')
    if len(tds) == 0:
        continue
    print(tds[0].get_text())