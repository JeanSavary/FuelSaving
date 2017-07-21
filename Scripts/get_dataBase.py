# -*- coding: utf-8 -*-
#    by Jean Savary

#--------------------------
#Importation des librairies 

import urllib
import os
import xml.etree.ElementTree as ET
import pandas as pd
import time
import zipfile

#--------------------------
#Définition du répertoire courant

os.chdir("/Users/MacbookJeansavary/Desktop/Programs/FuelSaving")

#--------------------------
#Opérations de téléchargement et stockage du fichier zip contenant la dataBase

def get_xml_from_web() :

    saved_zip = open('Data/Daily_prices.zip',"w")
    zip_file = urllib.urlopen('https://donnees.roulez-eco.fr/opendata/jour').read()
    saved_zip.write(zip_file)

    #--------------------------
    #Opération de dézippage du fichier zip afin d'en extraire le fichier xml / Suppression du fichier zip précédent
    unzip_file = zipfile.ZipFile('Data/Daily_prices.zip','r')
    xml_file_name = unzip_file.namelist()[0]

    saved_xml_file = open(xml_file_name,'w')
    xml_file = unzip_file.read(xml_file_name)
    saved_xml_file.write(xml_file)
    
    return xml_file_name
#--------------------------
#test = get_xml_from_web()
#time.sleep(60)

tree = ET.parse("Data/PrixCarburants_quotidien_20170720.xml")
root = tree.getroot()

cities = []
ids = []
postal_codes = []
adresses = []

for pdv in root.findall('pdv') :

    iD = pdv.get('id')
    if len (iD) == 7 : 
        ids.append("0" + iD[:1])
        postal_codes.append("0" + iD[:4])
    else : 
        ids.append(iD[:2])
        postal_codes.append(iD[:5])
    
    cities.append(pdv.find('ville').text)
    adresses.append(pdv.find('adresse').text)

#--------------------------

data = {"City" : cities,
        "Adresse" : adresses, 
        "iD" : ids,
        "Postal_Code" : postal_codes
        }

dataFrame = pd.DataFrame(data)
csv_dataFrame = dataFrame.to_csv("DataBases/stations_dataBase.csv", encoding = 'utf-8')

#os.remove('Data/Daily_prices.zip')