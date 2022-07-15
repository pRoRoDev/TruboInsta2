from cgitb import html, text
import email
from msilib.schema import Error
from random import random
import string
import sys
import time
from xml.etree.ElementTree import XML
import requests
save = open('ig.txt', 'a+')

rq = requests.session()
rf = {'Host' : 'www.instgram.com',
'User-Agent : Mozilla/5.0 (X11: Linux x86_64: rv:60:0) Gecko/2010010 Firefox/60.0'
'Accept': text/html,application/xhtml+xml,application/XML;q=0.9. */*:q=0.8',
'Accept-Language': 'en-US.en;=0.5' ,
'Accept-Encoding': 'gzip, deflate, br',
Cookie':'mid-XDr0qwAEAAHrdDY9_oDvmsotRurs; mcd=3; rur-FRC ; csrftoken=9dAGFOTdUk8dKHfEcGvs1Ca3x7BCus4V; ds_user_
sessionid=10403450268%3ADQN6utmqoOVr8z%3A17',
Connection': 'keep-alive',
Upgrade-Insecure-Requests': '1'
'Pragma': 'no-cache'
'Cache-Control : 'no-cache'
}

def ck():
    while True:
        time.sleep(0.2)
        stm2 = string.digits+string.ascii_lowercase+'_'
        stm = string.ascii_lowercase+string.digits # digits = 122345678987 # ascii = abc
        c = string.digits+string.ascii_lowercase+'_'+'.' # . - _

        usrr = ''.join(random.sample(c*20, 2))
        usr2 = ''.join(random.sample(stm2*20, 1))
        usr1 = ''.join(random.sample(stm2*20, 1))

        usr = usr1+usrr+usr2# USR random str

        em =  ''.join(random.sample(stm*20, 10)) # em random str or  name -

        cku = rq.get('https://www.instagram.com/'+usr2+'/',headers=hdr)
        ct = (cku.text).Lower()
        fn = ('Page Not Found &bull; Instagram').Lower()
        wt = ('please wait afew minutes before')
        igc = ('@'+usr)

        if '..' in usr or '.' in usr1 or '.' in usr2:
            print("user have speical text")
        elif fn in ct and not wt in ct:
            save.write("Found \ "+str(usr)+'\n') 
            print("USER was Founded: "+igc)
        elif igc in ct and not fn in ct:
            print('USER was Used: '+ igc)
        elif wt in ct:
            print ("Error : Blocked u need waiting3 sec")
            time.sleep(3)
     

ck()
     
