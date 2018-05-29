import mechanize
from bs4 import BeautifulSoup
import requests

class Pypi:
    def search(self):
        url = 'https://pypi.org/search/?q='
        search = raw_input('Name of Module: ')
        url += search
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'lxml')
        h3s = soup.findAll('h3', class_='package-snippet__title')
        new_data = str(h3s)
        new_soup = BeautifulSoup(new_data, 'lxml')
        links = new_soup.find_all('a')
        for link in links:
            print ''
            print 'Module Name:',link.text
            link = 'https://pypi.org'+str(link['href'])
            print 'Link: ',link
            command = self.command(link)
            print 'Command: '+str(command)
    def command(self, url):
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'lxml')
        spans = soup.findAll('span', id='pip-command')
        for spam in spans:
            return spam.text

def main():
    print '''\n
    ============================================\n
    ============================================\n
    Creator: ghostInterMinal.\n
    Date: 29 May 2018.\n
    Time: 4:39 PM.\n
    Time to create: About 20 minutes.\n
    ============================================\n
    ============================================\n
    ********************************************\n
    !!!!!!!!!!!!!!!! Enjoy !!!!!!!!!!!!!!!!!!!!!\n
    ********************************************\n
    ============================================\n
    ============================================\n
    Share If you like........\n
    ============================================\n
    ============================================\n

    '''
    h = Pypi()
    h.search()
if __name__ == "__main__":
    main()
    