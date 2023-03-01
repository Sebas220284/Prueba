 
import json
import requests
import time
 
def menu():
    print('IP tacker')
    ip = input('Ingresa una IP: ')
    api = "http://ip-api.com/json/" + ip
    data = requests.get(api).json()
    print('Pais: ', data['country'])
    print('Latitud: ', data['lat'])
    print('Longitud: ', data['lon'])
    print('Escaneo completo.')
    time.sleep(1)
    exit()
   
menu()