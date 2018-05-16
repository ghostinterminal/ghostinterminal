import mechanize
from bs4 import BeautifulSoup
import sys

url = str(sys.argv[1])
br = mechanize.Browser()
br.set_handle_robots(False)
data = br.open(url).read()
soup = BeautifulSoup(data, 'lxml')
links = soup.find_all('a')
for link in links:
    try:
    	l = str(link['href'])
    	if l.startswith('#'):
        	pass
    	else:
        	print l
    except:
	  print 'Error'
