from lib.interface import *
from time import sleep


while True:
    resp = menu('sistema de cadastro')
    if resp == 1:
        print('opc 1')
    elif resp == 2:
        print('opc 2')
    elif resp == 3:
        print('opc 3')
    else:
        print('Digite uma opção válida!')
    sleep(2)
    