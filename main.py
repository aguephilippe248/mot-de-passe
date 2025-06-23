# mot-de-passe
# PIRATE NOIR

print("Bienvenu dans le générateur de mot de passe du pirate Noir !!")
print()
import string
import random

def définition_du_mot_de_passe(longeur):

    # Fusionner les différents caractères 
    caractère=string.punctuation+string.ascii_letters+string.digits

    # Crée le mot de passe avec la longeur choisie par l'utilisateur 
    
    mot_de_passe= "".join(random.choice(caractère)for i in range(longeur))
    return mot_de_passe
    
# Demander à l'utilisateur de choisir la longueur de son mot de passe 
# Gestion des erreurs eventuelles 

while True:
    try :
        longeur=int(input("Votre mot de passe doit contenir compbien de lettre ? : "))
        if longeur <=3:
            print("Nous ne pouvons pas générer un mot de passe inférieur ou égale à 3")
            print("Merci de reprendre ")
        else:
            break # sortir si la valur est corrcete 
    except ValueError :
        print("ERREUR: Vous devez mettre uniquement que des chiffres ")
        print("Merci de reprendre ")
        print()



# Appel de la fonction et afficher le mot de passe 
mot_de_passe=définition_du_mot_de_passe(longeur)
print(f"Votre Mot de passe est : {mot_de_passe}")
print()
print("Merci et à bientot ")

