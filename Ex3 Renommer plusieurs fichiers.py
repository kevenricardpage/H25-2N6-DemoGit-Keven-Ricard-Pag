# importez os
# # allez dans le dossier Ex3 Videos
# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier

import os

os.chdir("c:\\Ex3 Videos")
status = os.getcwd()
fichiers = os.listdir()
for dossier in fichiers:
    nom,ext = os.path.splitext(dossier)
    titre,cours,num_cours = dossier.split('_')
    titre.strip()
    num_cours.strip()
    num_cours.zfill(1)
    print(dossier)

os.chdir("c:\\Ex3 Videos")
os.rename("Ex3 Videos", "Test")