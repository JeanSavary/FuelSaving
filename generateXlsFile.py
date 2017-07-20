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
dep = []
dataBase = {}


