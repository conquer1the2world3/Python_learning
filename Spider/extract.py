from bs4 import BeautifulSoup
import requests

url = 'https://cn.bing.com'

response = requests.get(url)
response.encoding = 'utf-8'
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').text
    print(title)
    print('--------------------------------')

first_link = soup.find('a')
print(first_link)
print('--------------------------------')
first_link_href = first_link.get('href')
print(first_link_href)
print('--------------------------------')
links = soup.find_all('a')
for link in links:
    print(link.get('href'))

all_text = soup.get_text()

search_box = soup.find('input', {'id': 'sb_form_q'})
print(search_box)


search_box_value = search_box.get('value')
print(search_box_value)
print('--------------------------------')

est_element = soup.select('div.est_common est_selected')
print(est_element)
print('--------------------------------')

links = soup.select('a[href^="https"]')
for link in links:
    print(link.get('href'))

# print(soup.prettify())  
