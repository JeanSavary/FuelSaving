# -*- coding: utf-8 -*-
#    by Jean Savary

#--------------------------
#Importation des librairies 

from bs4 import BeautifulSoup
import requests
import xlutils
import urllib
#--------------------------

dataBase = {}
url= "https://www.zagaz.com/prix-carburant.php?id_div=10"
web_page = urllib.urlopen(url)
source = web_page.read().decode('utf-8')



#--------------------------

def recherche_index_mot(source, mot_a_trouver) : #recherche_mot est une fonction permettant de trouver l'index de la dernière lettre d'un mot recherché au sein d'une chaine de caractères, ne pas oublier d'ajouter une entete de longueur supérieure à len(mot_a_trouver) lors du test de la fonction

    nb_char = len(mot_a_trouver)
    tmp_word = ""
    index = 0
    index_source = 0 #index de la dernière lettre du mot recherché
    rest_source = source[nb_char : ] #on enlève la partie de la source qui nous a servi à initialiser le tmp_word, ceci ne pose pas de pb car cela va supprimer l'entête du fichier html qui ne nous intéresse pas
    word_in_list = [] #il est plus simple de modifier des listes que des chaines de caractères, on met donc chaque lettre du mot_a_trouver dans une liste, ex : ["m","a","r", ...]
    list_index_source = []

    while index < nb_char : #initialisation de tmp_word
        tmp_word = tmp_word + source[index]
        index += 1
        index_source += 1
        
    #print (test_word, index_source, nb_char)
    
    for char in tmp_word :
        word_in_list.append(char)
        
    for char in rest_source : 
        
        for j in range (0, nb_char-1) :
            
            word_in_list[j] = word_in_list[j+1]
            
        word_in_list[nb_char-1] = char
      
        index_source += 1
        word_to_find = ""
        
        for element in word_in_list :
            
            word_to_find = word_to_find + element
        
       
        if word_to_find == mot_a_trouver : 

            list_index_source.append(index_source - 1)
    
    return list_index_source
#--------------------------

def affichage_mot(source, index_mot, limit_char) : #affichage_mot est une fonction qui permet d'afficher un caractère à partir de son index, cela permet aussi, via le paramètre "longueur_mot" d'afficher un mot à partir d'un index donné. Cette fonction permet en outre de controler le résultat donné par la fonction recherche_index_mot.
    
    mot = ""
    i = index_mot + 1
    
    while source[i] != limit_char :
        mot = mot + source[i]
        i += 1
    
    return mot
#--------------------------

liste_region = []
for elem in recherche_index_mot(source, '"fa fa-right-dir"></i><strong>') :
    liste_region.append (affichage_mot(source), elem, "<")
print (liste_region)