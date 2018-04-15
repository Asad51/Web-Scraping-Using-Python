import requests
import bs4;

getNums = requests.get('http://www.educationboardresults.gov.bd/')
soup = bs4.BeautifulSoup(getNums.content, 'lxml')
table = soup.find('table', {'class':'black12bold'})
tr = table.find_all('tr')
tds = tr[6].find_all('td')
txt = tds[1].get_text()
bot = str(eval(txt))
print(txt + ' = ' + bot)

post = requests.post('http://www.educationboardresults.gov.bd/result.php', data=dict(button2 = 'Submit', exam = 'hsc', year = '2014', board = 'dhaka', roll = '119416', reg = '848113', value_s = bot))
process = bs4.BeautifulSoup(post.content, 'lxml')
result = process.find_all('table', {'class':'black12'})
print(len(result))
print(process)
#result = process.find_all('table', {'class':'black12'})
#for tr in result.find_all('tr'):
#    tds = tr.find_all('td')
#    print(tds[0].get_text() + '\t' + tds[1].get_text() + '\t' + tds[2].get_text())