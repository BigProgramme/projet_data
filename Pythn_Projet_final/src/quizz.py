'''

Created Date: Wed Oct 26 2022
Author: Saint HEraud
-----
Last Modified: Wed Oct 26 2022
Modified By: Saint Heraud

'''

import random
from src.data import read_data_aop


# tirage_ville()
def quizz_1():
    read = read_data_aop("../data/aop.csv")
    commune_aop = read["Commune"]
    tirage = random.choice(commune_aop)
    point = 0

    aop_ville_tirage = read.loc[read["Commune"] == tirage, "Aire géographique"]
    stock_aop = list(aop_ville_tirage)
    stock_answer = []
    print("La ville tirée est : ", tirage + "\n" + "Il existe ", len(aop_ville_tirage), "AOPs à ", tirage)
    print("Vous allez entrer les noms des AOPs, TAPEZ 0 POUR ARRÊTER DE RENTRER")

    # for i in range(1, len(stock_aop) + 1):
    for i in range(1, len(stock_aop) + 1):
        get_aop = input("Entre les Aop de la ville de cette ville --->: ")
        stock_answer.append(get_aop)
        if i == 2:
            for answer in stock_answer:
                if get_aop == answer:
                    print("Vous l\'aviez déjà rentré")
                    point = point  # Le pas de point si ça existe
                break
        for j in stock_aop:
            if get_aop == j:
                print("Bonne réponse")
                point += 1
            else:
                point += 0
        print("vous avez :", point, "bonnes réponses")
    print("VOICI VOS REPONSES:")
    return stock_answer


print(quizz_1())
