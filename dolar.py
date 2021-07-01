from datetime import date
today = date.today()
import PySimpleGUI as sg
import requests
from bs4 import BeautifulSoup
import psycopg2     

conn = psycopg2.connect(database="dolar", user='postgres', 
password='qwe12345', host='127.0.0.1', port= '5432')
conn.autocommit = True 
cursor = conn.cursor() 


definir_site=requests.get('https://dolarhoje.com')
função_de_funcionamento = BeautifulSoup(definir_site.content, 'html.parser')
procurar_linha = função_de_funcionamento.find(id = 'nacional')
linha_convertida_para_caracteres=str(procurar_linha)
valor_em_real=(linha_convertida_para_caracteres[-7:-3])
print('UM REAL EM DOLAR ESTÁ VALENDO HOJE: : ', valor_em_real, "DOLARES")
sql=('''INSERT INTO DADOS VALUES (%s, %s)''')
val= (valor_em_real, today)
cursor.execute(sql, val)
from time import sleep
sleep(1)

definir_site = requests.get('https://www.euro-hoje.com/')
função_de_funcionamento = BeautifulSoup(definir_site.content, 'html.parser')
procurar_linha = função_de_funcionamento.find(id="nacional")
linha_convertida_para_caracteres=str(procurar_linha)
valor_em_real=(linha_convertida_para_caracteres[-7:-3])
print('UM REAL ESTÁ VALENDO HOJE: ', valor_em_real, "EUROS")
from time import sleep
sleep(1)
