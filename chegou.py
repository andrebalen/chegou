#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Licença: GPLv3

from bs4 import BeautifulSoup
import urllib2
# para usar expressoes regulares
#import re
# para usar itens do sistema
import os
import sys
#import csv
#import time

# informacoes para teste
# PL438427580BR
# http://www.linkcorreios.com.br/PL438427580BR

url = "http://www.linkcorreios.com.br/" #site de consulta a encomendas

# pega o rastreio passado como parametro
try:
    f = sys.argv[1]
except IndexError:
    f = "PL438427580BR"
    print '\033[32m'+'Codigo de Rastreio ausente, utilizar chegou.py CODIGO'+'\033[0;0m'
    print u' utilizando um teste ...'

new_url = url+f # concatena o rastreio a url

if f != None: # se tem boi na linha consulta
    content = urllib2.urlopen(new_url).read()
    soup = BeautifulSoup(content)
    # imprimir soh um intervalo ou a div com tag class="container"
    state = soup.find_all("div", class_="container")
    # imprime a primeira ocorrencia e converte as tags para texto
    print state[0].get_text()
#    print soup.prettify()[3330:4100]
    #print soup.td
