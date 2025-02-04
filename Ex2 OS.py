import os
os.chdir(os.path.dirname(__file__)) # cette ligne change le répertoire courant pour qu'il devienne celui où ce trouve le fichier actuel.

# Q1  Imprimez le répertoire courant
print(f"Q1{'_'*60}")

location = os.getcwd()

print(location)

# Q2   Imprimez la variable d'environnement USERPROFILE (utilisez la méthode .get() de l'objet os.environ)
print(f"Q2{'_'*60}")

user = os.environ.get("USERPROFILE")

print(user)


# Q3 Déplacez-vous sur le répertoire 'Documents' et imprimez le répertoire courant
#       Attention : n'utilisez pas un chemin relatif.
print(f"Q3{'_'*60}")

os.chdir("c:\\users\\1209410\\Documents")
nouvelle_location = os.getcwd()
print(nouvelle_location)



# Q4   Imprimez la liste des répertoires et des fichiers qu'il y a dans 'Document'
print(f"Q4{'_'*60}")

rep_fichier = os.listdir()

print(rep_fichier)



# Q5   Créez un répertoire OS-ExercQ5
#       Réimprimez les répertoires et les fichiers dans 'Document'
print(f"Q5{'_'*60}")

os.makedirs("OS-ExercQ5", exist_ok=True)

rep_fichier_nouveau = os.listdir()

print(rep_fichier_nouveau)


# Q6   Créez les répertoires OS-ExercQ6/Subdir1 avec une seule instruction
#       Réimprimez les répertoires et les fichiers dans votre 'Document'
print(f"Q6{'_'*60}")

os.makedirs("OS-ExercQ6/Subdir1",exist_ok=True)

rep_fichier_deux = os.listdir()

print(rep_fichier_deux)

#Q7   Renommez le répertoire Subdir1 pour qu'il s'appelle Sous_repertoire
print(f"Q7{'_'*60}")

os.chdir("c:\\users\\1209410\\Documents\\OS-ExercQ6")
renommer = os.rename("Subdir1","Sous_repertoire")

# Q8   suppression du répertoire OS-ExercQ6 et de son contenu
#       Réimprimez les répertoires et les fichiers dans votre 'Document'
print(f"Q8{'_'*60}")

os.rmdir("Sous_repertoire")
os.chdir("c:\\users\\1209410\\Documents")
os.rmdir("OS-ExercQ6")

rep_fichier_trois = os.listdir()

print(rep_fichier_trois)
