import requests
import bs4

##Filtering products
print('=========================================')
print('___________Filtering Products____________')
products = requests.post('http://localhost/foodsite/products.php', data=dict(filter_products='Filter Products', category_id='8'))
soup = bs4.BeautifulSoup(products.content,'lxml')
table = soup.find('table', {'class':'information_table'})
for tr in table.find_all('tr'):
    tds = tr.find_all('td')
    if len(tds) == 0:
        continue
    print(tds[0].get_text() + '-->' + tds[1].get_text())

##Clearing filter
print('========================================')
print('____________Clearing Filter_____________')
products2 = requests.post('http://localhost/foodsite/products.php', data=dict(clear_filter='Clear Filter'))
soup2 = bs4.BeautifulSoup(products2.content,'lxml')
table2 = soup2.find('table', {'class':'information_table'})
for tr2 in table2.find_all('tr'):
    tds2 = tr2.find_all('td')
    if len(tds2) == 0:
        continue
    print(tds2[0].get_text() + '-->' + tds2[1].get_text())
    
