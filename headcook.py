import requests
import base64
from bs4 import BeautifulSoup
import sys


url = str(sys.argv[1])

def decoration(element):
	print '--------------------------------------------'
	print element
	print '--------------------------------------------'


def headers_giving(url):
	print ''
	data = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240'})
	print '============= HEDAERS =================='
	for key in data.headers.keys():
		print key,' : ',data.headers[key]
	print '============= HEADERS =================='
	print 'Done....'
def cookies_giving(url):
	data = requests.post(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240'})
	print '============== COOKIES ==============='
	try:
	    for key in data.cookies.keys():
		print key,' : ',data.cookies[key]

	except:
		print 'Cookies not found..'
		print 'Good Luck...'
	print '============== COOKIES ==============='
if __name__ == '__main__':
	headers_giving(url)
	cookies_giving(url)
	


