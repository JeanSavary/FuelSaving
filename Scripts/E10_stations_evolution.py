# -*- coding: utf-8 -*-
#    by Jean Savary

#--------------------------
#Importation des librairies 

import os
import path
import numpy as np
import pandas as pd

#--------------------------
#Définition du répertoire courant
path = "/Users/MacbookJeansavary/Desktop/Programs/FuelSaving"
os.chdir(path)

#Création du csv contenant l'évolution du prix de l'E10 dans les différentes stations
list_files = os.listdir(path + "/DataBases")
dates = np.array(['Stations'])
index_colum = 0


for data_name in list_files[2:] : 

    np.append(dates,data_name[18:])
    #studied_dataBase = pd.read_csv(path + '/DataBases/' + data_name)
    dataframe = pd.DataFrame(data = dates)
    print(dataframe)

#datab = pandas.read_csv()
