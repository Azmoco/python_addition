"""Ce programme est un jeu où 10 additions, soustractions ou multiplications seront proposées.
l'utilisateur doit répondre le mieux possible aux calculs. le score est donné a la fin.
Auteurs : Corentin et Thibault"""

from random import randint
import sys
import time

def operation():
    """demande le type d'opérations"""
    type_operation = 0
    while type_operation not in ('addition', 'soustraction', 'multiplication'):
        type_operation = input("""Quelle opération voulez-vous faire ?
(tapez aide pour ouvrir une page d'aide)\n""")
        if type_operation == "aide":
            print("""
Pour obtenir 10 additions, ecrivez "addition"\n
Pour obtenir 10 soustraction, ecrivez "soustraction"\n
Pour obtenir 10 multiplication, ecrivez "multiplication"\n
            """)
        elif type_operation not in ('addition', 'soustraction', 'multiplication'):
            print("""Erreur_1: Votre réponse est invalide. il faut inscrire "addition" ,
"soustraction" ou "multiplication".\n""")
    return type_operation


def lit_nombre_chiffre():
    """demande le nombre de chiffre voulu pour les operations"""
    nombre_chiffre = input("Combien voulez-vous de chiffre dans vos opérations?\n")
    while nombre_chiffre == "0" or not nombre_chiffre.isnumeric():
        print("Erreur_2: Veuillez entrer un nombre entier supérieur à 0")
        nombre_chiffre = input("Combien voulez-vous de chiffre dans vos opérations?\n")
    nombre_chiffre = int(nombre_chiffre)
    return nombre_chiffre

def lit_pseudo():
    """demande le pseudo de l'utilisateur"""
    pseudo = input("Quel est votre pseudo?\n")
    while len(pseudo) < 3 or ' ' in pseudo:
        print("Veuillez entrer un pseudo d'au moins 3 caracteres et sans espace")
        pseudo = input("Quel est votre pseudo?\n")
    return pseudo

def lit_ancien_score(pseudo):
    """donne l'ancien score"""
    apparition_pseudo = 0
    fichier = open('scores.txt', 'r', encoding='utf8')
    liste_ligne = fichier.readlines()
    for ligne in liste_ligne:
        ligne = ligne.split()
        if pseudo == ligne[0]:
            ancien_score = int(ligne[len(ligne) - 1])
            ligne = " ".join(ligne)
            print(ligne)
            apparition_pseudo += 1
    if apparition_pseudo == 0:
        print("Bienvenue nouveau joueur!")
        ancien_score = 0
    fichier.close()
    return ancien_score

def donne_reponse_addition(valeur_max, temps_maximum):
    """affiche les 10 additions puis donne le nombre de bonnes reponses"""
    reponses_justes = 0
    compteur = 0
    while temps_maximum > time.time() and compteur < 10:
        valeur1 = randint(0, valeur_max)
        valeur2 = randint(0, valeur_max)
        calcul = valeur1 + valeur2
        print("\n" + str(valeur1) + " + " + str(valeur2))
        reponse_utilisateur = input("Quel est le résultat de ce calcul ? ")
        while not reponse_utilisateur.isdigit():
        #verif reponse_utilisateur soit des chiffres
            print("""Erreur_3: Votre réponse est invalide,
merci d'écrire uniquement des chiffres ou nombres""")
            reponse_utilisateur = input("Quel est le résultat de ce calcul ? ")
        if time.time() > temps_maximum:
            affiche_message()
            break
        if int(reponse_utilisateur) == int(calcul):
            reponses_justes += 1
        compteur += 1
    return reponses_justes


def donne_reponse_soustraction(valeur_max, temps_maximum):
    """affiche les 10 soustractions puis donne le nombre de bonnes reponses"""
    reponses_justes = 0
    compteur = 0
    while temps_maximum > time.time() and compteur < 10:
        valeur1 = randint(0, valeur_max)
        valeur2 = randint(0, valeur_max)
        if valeur1 < valeur2:
            valeur1, valeur2 = valeur2, valeur1
        calcul = valeur1 - valeur2
        print("\n" + str(valeur1) + " - " + str(valeur2))
        reponse_utilisateur = input("Quel est le résultat de ce calcul ? ")
        while not reponse_utilisateur.isdigit():
            print("""Erreur_3: Votre réponse est invalide,
merci d'écrire uniquement des chiffres ou nombres""")
            reponse_utilisateur = input("Quel est le résultat de ce calcul ? ")
        if time.time() > temps_maximum:
            affiche_message()
            break
        if int(reponse_utilisateur) == int(calcul):
            reponses_justes += 1
        compteur += 1
    return reponses_justes

def donne_reponse_multiplication(valeur_max, temps_maximum):
    """affiche les 10 multiplications puis donne le nombre de bonnes reponses"""
    reponses_justes = 0
    compteur = 0
    while temps_maximum > time.time() and compteur < 10:
        valeur1 = randint(0, valeur_max)
        valeur2 = randint(0, valeur_max)
        calcul = valeur1 * valeur2
        print("\n" + str(valeur1) + " x " + str(valeur2))
        #utilisation de "x" pour que l'utilisateur comprenne * plus facilement
        reponse_utilisateur = input("Quel est le résultat de ce calcul ? ")
        while not reponse_utilisateur.isdigit():
            print("""Erreur_3: Votre réponse est invalide,
merci d'écrire uniquement des chiffres ou nombres""")
            reponse_utilisateur = input("Quel est le résultat de ce calcul ? ")
        if time.time() > temps_maximum:
            affiche_message()
            break
        if int(reponse_utilisateur) == int(calcul):
            reponses_justes += 1
        compteur += 1
    return reponses_justes

def relancer_programme():
    """sert à relancer le programme si l'utilisateur le souhaite"""
    demande_relance = input("Voulez-vous relancer le programme ?\n")
    while demande_relance not in ('oui', 'non'):
        print("""Veuillez répondre "oui" ou "non".""")
        demande_relance = input("Voulez-vous relancer le programme ?\n")
    if demande_relance == "non":
        demande_relance = None
        print("Au revoir, à bientôt.")
        time.sleep(3)
        sys.exit()
    main()

def lit_temps_voulu():
    """demande le temps voulu pour realiser les calculs"""
    temps_voulu = input("Combien voulez-vous de temps (en secondes) pour faire vos calculs?\n")
    while not temps_voulu.isnumeric():
        print("Veuillez entrer un nombre entier supérieur ou égal à 5")
        temps_voulu = input("Combien voulez-vous de temps (en secondes) pour faire vos calculs?\n")
    temps_voulu = int(temps_voulu)
    while temps_voulu < 5:
        print("Veuillez entrer un nombre entier supérieur ou égal à 5")
        temps_voulu = input("Combien voulez-vous de temps (en secondes) pour faire vos calculs?\n")
        temps_voulu = int(temps_voulu)
    return temps_voulu

def affiche_message():
    """affiche un message lorsque le temps est ecoule"""
    message = randint(0, 100)
    if message <= 25:
        print("\nVous n'avez plus de temps !\n")
    if 25 < message <= 50:
        print("\nLe temps imparti est arrivé à expiration\n")
    if 50 < message <= 75:
        print("\nVous etes arrivé a la fin du temps imparti !\n")
    if 75 < message <= 99:
        print("\nVous n'avez pas eu le temps de finir, dommage :(\n")
    if message == 100:
        print("""\nBravo vous avez reussi... Ah non excusez-moi
        je me suis trompe, le temps est ecoule'\n""")
    # easter egg

def ecrit_nouveau_score(pseudo, nouveau_score):
    """ecrit le nouveau score dans le fichier"""
    fichier = open('scores.txt', 'r', encoding='utf8')
    lignes = fichier.readlines()
    fichier.close()
    chaine = str(pseudo) + " votre score est " + str(nouveau_score) + "\n"
    for i in range(len(lignes)):
        lig = lignes[i].split()
        if pseudo == lig[0]:
            lignes[i] = chaine
            fichier = open('scores.txt', 'w', encoding='utf8')
            fichier.write("".join(lignes))
            fichier.close()
            return
    fichier = open('scores.txt', 'a', encoding='utf8')
    fichier.write(chaine)
    fichier.close()

def main():
    """fonction globale avec pour objectif de faire fonctionner le programme"""
    print("Bonjour,\n\
Ce programme sert à générer 10 opérations de 3 types différents :\
multiplication, addition et soustraction\n")
    pseudo = lit_pseudo()
    ancien_score = lit_ancien_score(pseudo)

    type_operation = operation()

    nombre_chiffre = lit_nombre_chiffre()
    valeur_max = int(nombre_chiffre * "9")

    temps_voulu = lit_temps_voulu()
    temps_maximum = time.time() + temps_voulu

    if type_operation == "addition":
        affiche_operation = donne_reponse_addition(valeur_max, temps_maximum)
    elif type_operation == "soustraction":
        affiche_operation = donne_reponse_soustraction(valeur_max, temps_maximum)
    elif type_operation == "multiplication":
        affiche_operation = donne_reponse_multiplication(valeur_max, temps_maximum)

    reponses_justes = affiche_operation

    print("""Votre nombre de reponse(s) juste(s) est {}\n""".format(reponses_justes))
    nouveau_score = ancien_score + reponses_justes
    print("""Votre nouveau score est {}\n""".format(nouveau_score))
    ecrit_nouveau_score(pseudo, nouveau_score)

    relancer_programme()


main()
