import urllib.request, urllib.error


try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print(f'\033[0;31mO site pudim não está acessível!\033[m')
else:
    print(f'\033[0;32mConsegui acessar o site pudim com sucesso!\033[m')
