# Made By: Jatin Kumar
# You can chage these codes According to your need.`
# Thanks for using me..
# I am 12th Standard Boy..



# REQUIREMENTS: requests, BeautifulSoup

# STEPS FOR INSTALLATION OF REQUIREMENTS(In case you dont know.):

# For requests:- pip install request or sudo apt-get install python-requests.
# For BeautifulSoup:- pip install bs4 or sudo apt-get install python-bs4.



import os
import requests
from bs4 import BeautifulSoup


class Tool:
	def __init__(self):
		self.file_name = ''
		self.cwd = os.getcwd() # Current directory

		self.bigData = '' # Writing the file with this data

	def createFolder(self, name): # Make folder with given name in current dir.
		os.mkdir(str(self.cwd)+str(name))
		return 'Folder Created... {0}'.format(str(self.cwd)+str(name))

	def createFile(self,name): # Make file in current dir. 
		self.f = open(name, 'ab')
		print 'File Created {0}/{1}'.format(self.cwd, name)

	def writeFile(self): # Start writing the opened file with bigDatay
		print 'Writing in file...'
		self.f.write(self.bigData)
		print 'Done writing..'

	def closeWritingFile(self): # Closing the writing file
		self.f.close()
	

	def openUrl(self, url):
		# Function used to open the url and extract raw data.
		header  = {'User-agent':'Mozzila/5.0'}
		req = requests.get(url, headers=header)
		data = req.text
		self.keys = 'facebooklinkedintwtteryoutubegoogleinstagramsnapchatgoogle+'
		soup = BeautifulSoup(data, 'lxml')

		dataList = []

		links = soup.findAll('a')

		try:
			for link in links:
				for x in link['href'].split('.'):
					if self.isPresent(x) >= 1:
						if link not in dataList:
							dataList.append(link['href'])
		except:
			pass


		self.bigData = ',\n'.join(dataList)


	def isPresent(self,x):
		count = 0
		if x in self.keys:
			count += 1
		return count





 

def Banner():
	banner = '''\n
	========================|################|======================
	========================| START SCRAPING |======================
	========================|################|======================

	Thanks for using...



	'''
	return banner



def giveLinks():
	print Banner()
	path = raw_input('Please Enter the Path of File to Scrap: ')
	try:
		f = open(path)
	except:
		pass
	x = f.read()
	return x.split(',')

def main():

	tool = Tool()

	count = 0
	print '====================:Starting:==================='
	links = giveLinks()
	for link in links:
		tool.openUrl(link)
		tool.createFile(str(link.split('.')[1])+str(count)+'.csv')
		tool.writeFile()
		tool.closeWritingFile()
		count += 1
		print 'Done....{0} Url'.format(count)


if __name__ == '__main__':
	main()







