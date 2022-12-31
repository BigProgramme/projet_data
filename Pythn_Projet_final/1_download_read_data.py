'''
File: 1_download_read_data.py
Created Date: Wed Oct 26 2022
Author: Ammar Mian
-----
Last Modified: Wed Oct 26 2022
Modified By: Ammar Mian
-----*
Copyright (c) 2022 Université Savoie Mont-Blanc
-----
'''

from src.data import download_data , read_data_aop, read_data_commune

if __name__ == "__main__":

    # Download data if it doesn't exists
    url_aop = "https://www.data.gouv.fr/fr/datasets/r/38276359-ca66-4566-b4c5-f012286a77b4"
    download_data(url_aop, "./data/", "aop.csv")
    url_communes = "https://france-geojson.gregoiredavid.fr/repo/regions/auvergne-rhone-alpes/communes-auvergne-rhone-alpes.geojson"
    download_data(url_communes, "./data/", "communes_aires.geojson")

    aop = read_data_aop("./data/aop.csv")
    #Affichage des données du fichier CSV
    print(aop)

    commune = read_data_commune("./data/communes_aires.geojson")
    #Affichage des données geojson
    print(commune)
