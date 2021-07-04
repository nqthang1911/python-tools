import bs4
import requests
import io
response = requests.get('https://thangit.net/')
html_doc=response.text
file = io.open('code.html',mode='w',encoding='utf8')
file.write(html_doc)

soup = bs4.BeautifulSoup(html_doc,'html.parser')
eles = soup.select('title')

for ele in eles:
    print(ele.get_text())