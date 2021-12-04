from asks import *
import time
import random

tries_number = int(input(f"Combien vouleez-vous d'essais? Selectionnez un nombre entre 5 et {len(list_asks)}.\n>>"))


user = Player(tries_number)
time.sleep(1)
rules = """
    Les règles sont simples: à chaque question, on vous posera la question et on vous proposera trois réponses possibles.
    Parmi ces trois réponses, l'une est correcte, les deux autres sont fausses. Vous devrez écrire la réponse qui vous semble correcte.
    ATTENTION: Vous devez recopier la réponse sans faire de faute sans quoi la réponse sera comptée fausse. 
    Bonne chance... Vous en aurez besoin!

"""
print("Le Meilleur (Pire) Quiz de tous les temps !")
time.sleep(0.5)
print(rules)
time.sleep(0.5)


while user.tries > 0:

    while True:

        ask = random.choice(list_asks)

        if not str(ask) in user.have_been_ask:

            user.play(ask)
            time.sleep(1.5)
            print("----------------------")

            break


print(f"Bravo! Vous avez fini le quiz avec un score de {user.point} points sur {tries_number} questions ! Cela fait un ratio  d'aproximativent {int(100*user.point/tries_number)} %")
print("de bonnes réponses !")
input()