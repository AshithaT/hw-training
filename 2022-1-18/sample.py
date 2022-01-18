import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.tutorialspoint.com/tutorialslibrary.htm')
print("The status code is ", res.status_code)
print("\n")
soup_data = BeautifulSoup(res.text, 'html.parser')
print(soup_data.title)
print("\n")
print(soup_data.find_all('h4'))