#pip install bs4
#pip install lxml
import requests
from bs4 import BeautifulSoup
res = requests.get('http://www.naver.com')
soup=BeautifulSoup(res.text,'lxml')
a_tag=soup.a
print(type(a_tag))

print(a_tag)
