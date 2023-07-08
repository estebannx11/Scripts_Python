import colorama

import json
import requests
import time

colorama.init()

color_green = colorama.Fore.GREEN
color_blue = colorama.Fore.BLACK

dibujo = f"""
________$$$$$$$$$$________
_____d$$$$$$$$$$$$$b______
_____$$$$$$$$$$$$$$$$_____
____4$$$$$$$$$$$$$$$$F____
____4$$$$$$$$$$$$$$$$F____
____$$$$"_"$$$$"_"$$$$_____
_____$$F___4$$F___4$$_____
_____´$F___4$$F___4$"_____
______$$___$$$$___$P______
______4$$$$$"^$$$$$%_____
_______$$$$F__4$$$$_______
________"$$$ee$$$"________
________._*$$$$F4_________
_________$_____.$_________
_________"$$$$$$"_________
__________^$$$$___________
_4$$c_______""_______.$$r_
_^$$$b______________e$$$"_
_d$$$$$e__________z$$$$$b_
4$$$*$$$$$c____.$$$$$*$$$r
_""____^*$$$be$$$*"____^"_
__________"$$$$"__________
________.d$$P$$$b_________
_______d$$P___^$$$b_______
___.ed$$$"______"$$$be.___
_$$$$$$P__________*$$$$$$_
4$$$$$P____________$$$$$$"
_"*$$$"____________^$$P___
____""______________^"____
"""

dibujo_coloreado = color_green + dibujo + color_blue
print(dibujo_coloreado)


def menu():
  print('CONSULTAR IP')
  ip = input('Por favor ingresar la ip a consultar: ')
  api = "http://ip-api.com/json/" + ip
  data = requests.get(api).json() #info ip
  print('Estado: ', data['status'])
  #print('Continente: ', data['continentCode'])
  print('Pais: ', data['country'])
  print('Region: ', data ['region'])
  print('Ciudad: ', data['city'])
  print('Ciudad 2: ', data['regionName'])
  #print('Distrito: ', data['district'])
  print('Codigo Ciudad: ', data['countryCode'])
  print('Latitud: ', data['lat'])
  print('Longitud: ', data['lon'])
  print('Zona Horaria: ', data['timezone'])
  print('ISP: ', data['isp'])
  print('Organización: ', data['org'])
  #print('DNS: ', data['reverse'])
  #print('Conexion Mobil: ', data['movil'])
  print('Ip utilizada para la consulta: ', data['query'])
  print('Escaneo Compelto.')
  time.sleep(1)
  exit()

menu()