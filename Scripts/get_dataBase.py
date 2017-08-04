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

    saved_xml_file = open('Data' + '/' + xml_file_name,'w')
    xml_file = unzip_file.read(xml_file_name)
    saved_xml_file.write(xml_file)
    
    return xml_file_name
#--------------------------
xml_file_name = get_xml_from_web()
#time.sleep(60)

tree = ET.parse('Data' + '/' + xml_file_name)
root = tree.getroot()

PDV = root.findall('pdv')

cities = []
ids = []
postal_codes = []
adresses = []
count = 0

number_of_city = len(PDV)

SP95 = [''] * number_of_city
Gazole = [''] * number_of_city
SP98 = [''] * number_of_city
E10 = [''] * number_of_city

for pdv in PDV :

    adresse = pdv.find('adresse').text
    iD = pdv.get('id')

    if len (iD) == 7 : 
        ids.append("0" + iD[:1])
        postal_codes.append("0" + iD[:4])
    else : 
        ids.append(iD[:2])
        postal_codes.append(iD[:5])
    
    cities.append(pdv.find('ville').text)
    adresses.append(adresse)

    fuels = pdv.findall('prix')

    no_data = "Not available"
    SP95[count] = no_data
    SP98[count] = no_data
    Gazole[count] = no_data
    E10[count] = no_data

    for fuel in fuels :

        valeur = fuel.get('valeur')

        if fuel.get('nom') == 'SP95' : 
            SP95[count] = valeur[0] + "," + valeur[1:]
        elif fuel.get('nom') == 'SP98' :
            SP98[count] = valeur[0] + "," + valeur[1:]
        elif fuel.get('nom') == 'Gazole' :
            Gazole[count] = valeur[0] + "," + valeur[1:]
        elif fuel.get('nom') == 'E10' :
            E10[count] = valeur[0] + "," + valeur[1:]
    count += 1
#--------------------------
#print("SP95 : " + SP95[2], "SP98 : " + SP98[2], "Gazole : " + Gazole[2])

data = {"City" : cities,
        "Adresse" : adresses, 
        "iD" : ids,
        "Postal_Code" : postal_codes,
        "SP95" : SP95,
        "SP98" : SP98,
        "Gazole" : Gazole,
        "E10" : E10
        }
#print(len(SP95), len(SP98), len(Gazole), len(ids), len(postal_codes), len(cities), len(adresses))
dataFrame = pd.DataFrame(data)

csv_dataFrame = dataFrame.to_csv("DataBases/stations_dataBase_"+ xml_file_name[25:33] + ".csv", encoding = 'utf-8')

os.remove('Data/Daily_prices.zip')