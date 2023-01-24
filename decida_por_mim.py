#Faça uma pergunta ao programa e ele terá que te dar uma resposta
import random

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Eu faria isso com certeza',
            'Não sei não hein!',
            'Não faz isso por favor!',
            'Acho que voce deveria!',
            'Só faz!!'
        ]

    def iniciar(self):
        input("Faça sua pergunta:")
        print(random.choice(self.respostas))

decisao = DecidaPorMim()
decisao.iniciar()