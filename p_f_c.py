import random 

choix_possibles = ['pierre', 'feuille', 'ciseaux']

def jouer():
    choix_utilisateur = input("Choisissez pierre, feuille ou ciseaux : ").lower()
    if choix_utilisateur not in choix_possibles:
        print("Choix invalide. Veuillez réessayer.")
        return jouer()

    choix_ordinateur = random.choice(choix_possibles)
    print(f"L'ordinateur a choisi : {choix_ordinateur}")

    if choix_utilisateur == choix_ordinateur:
        print("Égalité !")
    elif (choix_utilisateur == 'pierre' and choix_ordinateur == 'ciseaux') or \
         (choix_utilisateur == 'feuille' and choix_ordinateur == 'pierre') or \
         (choix_utilisateur == 'ciseaux' and choix_ordinateur == 'feuille'):
        print("Vous avez gagné !")
    else:
        print("Vous avez perdu !")