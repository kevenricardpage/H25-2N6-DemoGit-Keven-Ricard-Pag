import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

# Importez csv

import csv
 

# Vous utiliserez encore le fichier "Ex7 Lan Party.csv"
# 
#         Créez une liste des jeux joués dans les différents Lan Party du fichier.
#         N'ajoutez à cette liste chaque jeu qu'une seule fois 
#                         (vérifiez si le jeu est dans la liste avant de l'ajouter
#                          vous pouvez vérifier avec l'instruction 'in'
#         Triez la liste en ordre aphabétique 
#         Finalement, imprimez la liste des différents jeux joués triés en ordre alphabétique


#         Si besoin, des instructions détaillées sont données plus bas

ficher_a_lire = os.path.join("csvs", "Ex7 Lan Party.csv")

jeu_jouer = []

with open(ficher_a_lire,"r",encoding="UTF-8") as fichier_lu:
    lecteur = csv.reader(fichier_lu,delimiter=";")
    next(lecteur)

    for jeu in lecteur:
        avoir_trois_jeu = jeu[1:4]
        for each_jeu in avoir_trois_jeu:
            if jeu_jouer.count(each_jeu) == 0 :
                jeu_jouer.append(each_jeu)
                jeu_jouer.sort()
                print(jeu_jouer)



            #jeu_jouer.append(jeu)
            #jeu_jouer.sort()
           # print(jeu_jouer)


# INSTRUCTIONS DÉTAILLÉES
#      Commencez par créer une liste des différents jeux vide
#      Ouvrez le fichier 'Ex4 Lan Party.csv' en lecture
#      utilisez csv.reader pour lire le fichier avec le bon delimiter
#      Sautez la première ligne de l'entête
#      Faites une boucle pour passer à travers chacune des lignes 
#      Utilisez le slicing pour garder uniquement les 3 jeux
#      Faites une boucle pour passer à travers chacun des jeux
#      Avec count, obtenez le nombre de fois que le jeu est dans votre liste des différents jeux
#      Si le count est de 0, vous ne l'avez jamais ajouté alors ajoutez le jeu à votre liste
#      En dehors de toute boucle, utilisez sorted() pour trier la liste et obtenir une nouvelle liste triée
#      Imprimez votre nouvelle liste triée


