# -*- coding: utf-8 -*-
#    by Jean Savary

#--------------------------
#Importation des librairies 

from bs4 import BeautifulSoup
import xlutils
import requests
import pandas as pd
import os
#--------------------------
#Définition du répertoire courant

os.chdir("/Users/MacbookJeansavary/Desktop/Programs/FuelSaving")
departements_file = open("departement.html","r")

#--------------------------
#Construction de la dataBase départements

source = departements_file.read()
soup = BeautifulSoup(source, 'html.parser')
liste = soup.find_all('a')
num = soup.find_all('li')
departements, departements_code = [], []

for elem in num :
    code = elem.contents[0].replace(":" , "")
    departements_code.append(code)

for elem in liste : 
    departements.append(elem.string)

'''   
#Correcting code for 9 first items
for i in range (10) :
    corrected_code = "0" + departements_code[i]
    departements_code[i] = corrected_code
'''

data = {"Département" : departements,
        "Code" : departements_code}

dataFrame = pd.DataFrame(data).to_csv("DataBase.csv", encoding = 'utf-8')

