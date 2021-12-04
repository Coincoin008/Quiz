import random



class Ask:

    def __init__(self, ask, correct_answer, possible_answers=(), point=1, shuffle=True):

        self.correct_answer = correct_answer.lower()
        self.point = point
        self.ask = ask
        self.possible_answers = possible_answers
        self.shuffle = shuffle



    def __str__(self):

        return self.ask

    def _try(self, answer_given):

        return answer_given.lower() == self.correct_answer.lower()




class Player:

    def __init__(self, tries=10):

        #self.pseudo = pseudo
        self.point = 0
        self.tries = tries
        self.have_been_ask = []

    def play(self, ask):

        if self.tries > 0:

            self.have_been_ask.append(str(ask))
            self.tries = self.tries - 1

            print(ask.ask)

            possible_answers = list(ask.possible_answers)
            possible_answers = ["-"+str(n) for n in possible_answers]

            if ask.shuffle == True:

                random.shuffle(possible_answers)

            print("\n".join(possible_answers))
            print("Quelle est la réponse correcte ?")
            answer_given = input(">>")

            if ask._try(answer_given) == True:

                print("Bravo! C'est la bonne réponse!")
                self.point = self.point + 1

            else:

                print(f"Ah... C'est la mauvaise réponse. La bonne réponse était {ask.correct_answer}")










