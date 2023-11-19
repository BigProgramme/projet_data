'''

Created Date: Wed Oct 26 2022
Author: Saint HEraud
-----
Last Modified: Wed Oct 26 2022
Modified By: Saint Heraud

'''

import numpy as np
import pandas as pd
from geopandas import *
import folium

from src.data import *

chemin_aop = "./data/aop.csv"
chemin_json = "./data/communes_aires.geojson"


# Fonction qui prend le nom d'une commune et renvoie toutes ces informations

def info_commune():
    # Le nom de la commune
    commune_name = input("Entrer le nom de la commune pour avoir ses informations: \n")

    # Lecture de notre doc

    read = pd.read_csv(chemin_aop, sep=";", encoding="ISO8859-1")

    # Récupération de la colonne commune et la comparer au nom de la commune
    # puis renvoyer les infos concernées

    commune = read["Commune"]
    return read[commune == commune_name]


# fonction qui élimine les doublons

def sans_doublons():
    aop = read_data_aop(chemin_aop)

    # On utilise subset pour spécifier la colonne dans laquelle
    # on va supprimer les doublons

    x = aop.drop_duplicates(subset=["Aire géographique"])
    return x["Aire géographique"]


# Aop et le nom des communes qui les produisent :
def aop_commune():
    aop_name = input("Entrer le nom de l\'AOP pour obtenir les communes qui le produisent: ")
    read = read_data_aop(chemin_aop)
    colonne_aop = read["Aire géographique"]
    if aop_name not in colonne_aop:
        print("LES DONNEES DE L\'AOP", aop_name, "SONT VIDES" + "\n" + "OU ELLE N\'EXISTE PAS")
    else:
        print("VOICI LES NOMS DES COMMUNES QUI PRODUISENT LE :", aop_name)

    # Sélection de lignes et/ou de colonnes spécifiques à l’aide de
    # l’utilisation de la ligne et les noms de colonnes avec la méthode .loc
    return read.loc[colonne_aop == aop_name, "Commune"]


# Afficher le nombre d’AOP par commune pour toutes les communes

def nbre_aop_commune():
    read = read_data_aop(chemin_aop)
    return read.groupby("Commune")["Aire géographique"].nunique()


# Afficher le nombre de communes par AOP pour les AOP
def nbre_aop_aop():
    read = read_data_aop(chemin_aop)
    return read.groupby("Aire géographique")["Commune"].nunique()


# Fonction qui prend deux codes postaux...
# Et renvoie la liste
def postal():
    print("NB: UN CODE POSTAL DOIT AVOIR 5 CHIFFRES" + '\n')
    valeur_min = input('Entrer la valeur minimale du code postal-->:')
    if len(str(valeur_min)) < 5:
        print("il doit avoir 5 chiffre pour le code postal" + "\n")
        valeur_min = input('Entrer la valeur minimale du code postal avec 5 chiffres (EX: 01001; 74000...) -->:' + '\n')
    valeur_max = input('Entrer la valeur maximale du code postal-->:')
    if len(str(valeur_max)) < 5:
        print("il doit avoir 5 chiffre pour le code postal" + "\n")
        valeur_max = input('Entrer la valeur maxi du code postal avec 5 chiffres (EX: 74600, 01100) -->:')
    read = read_data_aop(chemin_aop)
    code_postal = read["CI"]
    return read.loc[code_postal.between(valeur_min, valeur_max)]


def carte_ville_comte():
    read = read_data_aop(chemin_aop)
    commune = read_data_commune(chemin_json)
    nom_commune = commune["nom"]

    colonne_aop = read["Aire géographique"]

    colonne_aop_comte = read.loc[colonne_aop == "Comté", "Commune"]  # Récup des communes qui font du comté

    # récup des noms des villes dans le fichier geojson et vérification
    # si elles sont == celles des communes qui produisent du comté avec la méthode isin

    return commune[nom_commune.isin(colonne_aop_comte)]


def superficie():
    read = read_data_aop(chemin_aop)
    commune = read_data_commune(chemin_json)

    aop_to_calcul_area = input("Entrer le nom du aop pour calculer la superficie des ces communes:")

    colonne_aop_ = read.loc[read["Aire géographique"] == aop_to_calcul_area, 'Commune']

    existance = commune.loc[commune["nom"].isin(colonne_aop_), "geometry"]

    var = existance.area

    return sum(var * (10 ** 6))


# Fonction qui gère les choix des users
# Je prends le choix de l'utilisateur avec cette petite fonction

def get_choix():
    choix = ""
    try:
        choix = int(input("Entrer le numéro de la tâche que vous voulez exécuter-->: "))
    except ValueError:
        print("Oops! vous avez rentré un numéro invalide.")
        print("LE PROGRAMME S'ARRÊTE LA.")
    if choix == 1:
        res = read_data_aop(chemin_aop)
        print(res)
    elif choix == 2:
        read_data_commune(chemin_json).plot(figsize=(100, 100), edgecolor="k")
    elif choix == 3:
        print(info_commune())
    elif choix == 4:
        print(sans_doublons())
    elif choix == 5:
        print('\n')
        print(aop_commune())
    elif choix == 6:
        print(nbre_aop_commune())
    elif choix == 7:
        print(nbre_aop_aop())
    elif choix == 8:
        print(postal())
    elif choix == 9:
        carte_ville_comte().plot(figsize=(100, 100), edgecolor="k")
    elif choix == 10:
        print(superficie())
