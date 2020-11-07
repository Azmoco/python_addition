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


def affiche_addition(valeur_max, temps_maximum):
    """affichage de 10 additions"""
    reponses_juste = 0
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
            reponses_juste += 1
        compteur += 1
    return("""Votre nombre de reponse(s) juste(s) est {}\n""".format(reponses_juste))


def affiche_soustraction(valeur_max, temps_maximum):
    """affichage de 10 soustraction"""
    reponses_juste = 0
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
            reponses_juste += 1
        compteur += 1
    return ("""Votre nombre de reponse(s) juste(s) est {}\n""".format(reponses_juste))

def affiche_multiplication(valeur_max, temps_maximum):
    """affichage de 10 multiplication"""
    reponses_juste = 0
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
            reponses_juste += 1
        compteur += 1
    return ("""Votre nombre de reponse(s) juste(s) est {}\n""".format(reponses_juste))

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

def main():
    """fonction globale avec pour objectif de faire fonctionner le programme"""
    type_operation = operation()

    nombre_chiffre = lit_nombre_chiffre()
    valeur_max = int(nombre_chiffre * "9")

    temps_voulu = lit_temps_voulu()
    temps_depart = time.time()
    temps_maximum = temps_depart + temps_voulu

    if type_operation == "addition":
        affiche_operation = affiche_addition(valeur_max, temps_maximum)
    elif type_operation == "soustraction":
        affiche_operation = affiche_soustraction(valeur_max, temps_maximum)
    elif type_operation == "multiplication":
        affiche_operation = affiche_multiplication(valeur_max, temps_maximum)

    print(str(affiche_operation))

    print(relancer_programme())


main()
#décomposer les affiche_... car ces fonctions doivent juste afficher
