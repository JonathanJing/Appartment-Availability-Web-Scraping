import re
import urllib.request
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = 'https://www.liveataspect.com/availableunits.aspx'
headers={'User-Agent':user_agent,} 

request=urllib.request.Request(url,None,headers)
response = urllib.request.urlopen(request)
html = response.read()

soup = BeautifulSoup(html, "html.parser")
tags = soup('tr')

for tag in tags:
    name = tag.get_text(':')
    if re.findall('^#.4',name):
      name = name.split(':')
      if int(name[1]) > 1000:
        print(name)
