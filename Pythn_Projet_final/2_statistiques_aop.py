from src.statistiques import *

# Liste des taches
liste_tache = [

    "AFFICHAGE DU TABLEAU DE DONNEES AOP",
    "VISUALISATION DE LA CARTE DE COMMUNE",
    "AFFICHER LES INFORMATIONS D'UNE COMMUNE",
    "ELIMINER LES DOUBLONS DES AOP(AIRES GEOGRAPHIQUES) DU FICHIER CSV",
    "PRENDRE UN NOM d’AOP AFFICHER TOUTES LES COMMUNES QUI LE PRODUISENT",
    "AFFICHER LE NOMBRE D'AOP PAR COMMUNE POUR TOUTES LES COMMUNES",
    "AFFICHER LE NOMBRE DE COMMUNE PAR AOP POUR TOUS LES AOP",
    "AFFICHER TOUS LES AOP ENTRE DEUX CODES-POSTAUX",
    "AFFICHER LA CARTE DES VILLES PRODUISANT DU COMTE",
    "CALCULER LA SUPERFICIE TOTALE DES COMMUNES QUI PRODUISENT UNE AOP"

]

# Petit programme pour la beauté de l'output
print("\n")
print("Voici la liste de tâches:\n")
num_taches = 1
for taches in liste_tache:
    print("Tâche numéro:", num_taches, ":", taches + "\n")
    num_taches += 1

if __name__ == "__main__":
    print("\n")
    get_choix()
