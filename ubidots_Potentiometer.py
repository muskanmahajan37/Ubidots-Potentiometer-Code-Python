#!/usr/bin/python
import Netmaxiot
import time
import requests

def read_temp():
   
    
    read1 = Netmaxiot.analogRead(0)    
    print read1
    time.sleep(0.01)
    
    payload = {'Potentiometer':read1}
    return payload

while True:
        try:
            r = requests.post('http://things.ubidots.com/api/v1.6/devices/raspberry/?token=A1E-eAxvSNe0CePS8KBqPoRLNaXGfkZaEq', data=read_temp())
            print('sending our values to ubi dots ')
            print(read_temp())
        except:
            pass          
        time.sleep(10)
