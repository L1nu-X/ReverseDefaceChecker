import urllib
import urllib2
import re
import os
from time import sleep
def slow(text):
    for i in text:
        print i,
        sleep(.6)
print 'Welcome to deface checker from reverse ip by Choyon'
print 'Contact me: facebook.com/wax.vampire'
create_a_file = open('defaced.txt', 'w')
create_a_file.close()
create_a_file = open('error.txt', 'w')
create_a_file.close()
create_a_file = open('failed.txt', 'w')
create_a_file.close()
ip = raw_input('Enter the server url: \n')
print 'Performing reverse IP lookup.Please wait ...'
try:
    reverse_lookup = urllib.urlopen('http://api.hackertarget.com/reverseiplookup/?q=' + ip).read()
    if 'error check your search parameter' in reverse_lookup:
        print 'Your given domain seems incorrect!Please double check or reverse lookup is'
        print 'UNAVAILABLE for your domain!'
        input('Press enter to exit ...')
        exit(0)
except IOError:
    print 'Internet error or Reverse lookup server down!Try again!'
cache = re.findall('[\w.]+', reverse_lookup)
loop = 0
while loop < len(cache):
    print 'checking on,', cache[loop]
    if 'http://' not in cache[loop]:
        temp = 'http://' + cache[loop]
    else:
        temp = cache[loop]
    try:
        resp = urllib2.urlopen(temp).code
        if resp == 200:
            temp1 = urllib.urlopen(temp).read()
            if ('Hacked' or 'hacked') in temp1:
                print temp, 'is defaced!'
                save_to_file = open('defaced.txt', 'a')
                save_to_file.write(temp + '\n')
                save_to_file.close()
            elif ('Hacked' or 'hacked') not in temp1:
                print temp, 'is not defaced!'
                save_to_file = open('error.txt', 'a')
                save_to_file.write(temp + '\n')
                save_to_file.close()
    except urllib2.URLError, checkurl:
        if checkurl == 404:
            print temp, 'is not defaced!'
            save_to_file = open('error.txt', 'a')
            save_to_file.write(temp + '\n')
            save_to_file.close()
        else:
            print temp, 'is unreachable or doesn\'t exist'
            save_to_file = open('failed.txt', 'a')
            save_to_file.write(temp + '\n')
            save_to_file.close()
    loop += 1
slow('bye for now ...')
os.startfile('defaced.txt')
os.startfile('error.txt')
os.startfile('failed.txt')
