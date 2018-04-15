import requests
import bs4

page1 = requests.get('http://localhost/foodsite/index.php')
soup = bs4.BeautifulSoup(page1.content, 'lxml')
x1 = soup.find('input', {'name':'clear_search'})
print(x1.attrs)
print(x1['value'])
