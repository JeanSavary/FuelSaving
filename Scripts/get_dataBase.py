# -*- coding: utf-8 -*-
#    by Jean Savary

#--------------------------
#Importation des librairies 

import urllib
import lxml
import os
import zipfile

#--------------------------
#Définition du répertoire courant

os.chdir("/Users/MacbookJeansavary/Desktop/Programs/FuelSaving/Data")

#--------------------------
#Opérations de téléchargement et stockage du fichier zip contenant la dataBase
saved_zip = open('Daily_prices.zip',"w")
zip_file = urllib.urlopen('https://donnees.roulez-eco.fr/opendata/jour').read()
saved_zip.write(zip_file)

#--------------------------
#Opération de dézippage du fichier zip afin d'en extraire le fichier xml / Suppression du fichier zip précédent
unzip_file = zipfile.ZipFile('Daily_prices.zip','r')
xml_file_name = unzip_file.namelist()[0]

saved_xml_file = open(xml_file_name,'w')
xml_file = unzip_file.read(xml_file_name)
saved_xml_file.write(xml_file)

os.remove('Daily_prices.zip')