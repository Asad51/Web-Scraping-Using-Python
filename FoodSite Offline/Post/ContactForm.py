import requests
import bs4

form = requests.post('http://localhost/foodsite/contact.php', data=dict(send_email = 'Send Email', name = 'Asad', email = 'asad@ru.ac.bd', subject = 'common', message = 'Nothing to write'))
soup = bs4.BeautifulSoup(form.content, 'lxml')
x = soup.find('span', {'class':'error'})

print(x)