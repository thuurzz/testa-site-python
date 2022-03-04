from ast import Try
import csv
import requests
with open("links.csv") as arquivo:
    linhas = csv.reader(arquivo)
    for linha in linhas:
        link = linha[0].split(";")
        try:
            req = requests.get(link[0]).status_code
            print(f'Site: {link[0]} Status: [{requests.get(link[0]).status_code}]')
        except:
            sites_com_erro = open("sites-com-erro.csv", "a")
            sites_com_erro.write(f'{link[0]}\n')
            sites_com_erro.close()