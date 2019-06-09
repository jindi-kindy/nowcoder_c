# -*- coding: utf-8 -*-
# @Time    : 2019/6/9 19:51
# @Author  : jindi
# @FileName: c1.py.py

import requests
from bs4 import BeautifulSoup

content = requests.get("https://www.qiushibaike.com/text/").content
soup = BeautifulSoup(content,'html.parser')

for div in soup.find_all('div',{'class':'content'}):
    print(div.text.strip())
