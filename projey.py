from random import randint

def operation():
    type_operation = 0
    while type_operation != "addition" and type_operation != "soustraction" and type_operation != "multiplication":
        type_operation = input("""quelle opération voulez-vous faire ?
(tapez aide pour ouvrir une page d'aide)\n""")
        if type_operation == "aide":
            print("""
Pour obtenir 10 additions, ecrivez "addition"\n
Pour obtenir 10 soustraction, ecrivez "soustraction"\n
Pour obtenir 10 multiplication, ecrivez "multiplication"\n
            """)
        elif type_operation != "addition" and type_operation != "soustraction" and type_operation != "multiplication":
            print("""Erreur_1: Votre réponse est invalide. il faut inscrire "addition" ,
"soustraction" ou "multiplication".\n""")
    return type_operation


def lit_nombre_chiffre():
    """a"""
    nombre_chiffre = input("Combien voulez-vous de chiffre dans vos opérations?\n")
    valeur_max = 0
    while nombre_chiffre == "0" or not nombre_chiffre.isnumeric():
        print("Erreur_2: Veuillez entrer un nombre entier supérieur à 0")
        nombre_chiffre = input("Combien voulez-vous de chiffre dans vos opérations?\n")
    nombre_chiffre = int(nombre_chiffre)
    return nombre_chiffre


def affiche_addition(valeur_max):
    reponses_juste = 0
    for i in range(10):
        valeur1 = randint(0, valeur_max)
        valeur2 = randint(0, valeur_max)
        calcul = valeur1 + valeur2
        print(str(valeur1) + " + " + str(valeur2))
        reponse_utilisateur = input("Quel est le résultat de ce calcul ? ")
        while reponse_utilisateur.isdigit() == False: #verification si reponse_utilisateur ne comporte que des chiffres
            print("""Erreur_3: Votre réponse est invalide,
merci d'écrire uniquement des chiffres ou nombres""")
            reponse_utilisateur = input("Quel est le résultat de ce calcul ?")
        if int(reponse_utilisateur) == int(calcul):
            reponses_juste += 1
    return reponses_juste


def affiche_soustraction(valeur_max):
    reponses_juste = 0
    for i in range(10):
        valeur1 = randint(0, valeur_max)
        valeur2 = randint(0, valeur_max)
        if valeur1 < valeur2:
            valeur_echange = valeur1
            valeur1 = valeur2
            valeur2 = valeur_echange
        calcul = valeur1 - valeur2
        print("\n" + str(valeur1) + " - " + str(valeur2))
        reponse_utilisateur = input("Quel est le résultat de ce calcul ? ")
        while reponse_utilisateur.isdigit() == False:
            #verification si reponse_utilisateur ne comporte que des chiffres
            print("""Erreur_3: Votre réponse est invalide,
merci d'écrire uniquement des chiffres ou nombres""")
            reponse_utilisateur = input("Quel est le résultat de ce calcul ? ")
        if int(reponse_utilisateur) == int(calcul):
            reponses_juste += 1
    return reponses_juste

def affiche_multiplication(valeur_max):
    reponses_juste = 0
    for i in range(10):
        valeur1 = randint(0, valeur_max)
        valeur2 = randint(0, valeur_max)
        calcul = valeur1 * valeur2
        print(str(valeur1) + " x " + str(valeur2))
        #utilisation de "x" pour que l'utilisateur comprenne * plus facilement
        reponse_utilisateur = input("Quel est le résultat de ce calcul ? ")
        while reponse_utilisateur.isdigit() == False:
            #verification si reponse_utilisateur ne comporte que des chiffres
            print("""Erreur_3: Votre réponse est invalide,
merci d'écrire uniquement des chiffres ou nombres""")
            reponse_utilisateur = input("Quel est le résultat de ce calcul ? ")
        if int(reponse_utilisateur) == int(calcul):
            reponses_juste += 1
    return reponses_juste


def main():
    type_operation = operation()

    nombre_chiffre = lit_nombre_chiffre()
    valeur_max = int(nombre_chiffre * "9")

    if type_operation == "addition":
        affiche_operation = affiche_addition(valeur_max)
    elif type_operation == "soustraction":
        affiche_operation = affiche_soustraction(valeur_max)
    elif type_operation == "multiplication":
        affiche_operation = affiche_multiplication(valeur_max)

    print(str(affiche_operation))

main()
#décomposer les affiche_addition/affiche_soustraction/affiche_multiplication car ces fonctions doivent juste afficher
