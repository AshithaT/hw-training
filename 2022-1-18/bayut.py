from bs4 import BeautifulSoup
import requests
  
# get URL
url = 'https://www.bayut.com/to-rent/property/dubai/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
for link in soup.find_all('a'):
    print(link.get('href'))