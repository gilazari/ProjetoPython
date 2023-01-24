#Algoritmo que gera um numero e eu tenho que chutar ate acertar

import random

class ChuteUmNumero:
    def __init__(self):
        self.valoraleatorio = 0
        self.valorminimo = 0
        self.valormaximo = 100
        self.tentarnovamente = True

    def iniciar(self):
        self.gerarnumero()
        self.pergunta()
        while self.tentarnovamente == True:
            if int(self.chute) > self.valoraleatorio:
                print("Chute um valor mais baixo.")
                self.pergunta()
            elif int(self.chute) < self.valoraleatorio:
                print("Chute um valor mais alto.")
                self.pergunta()
            elif int(self.chute) == self.valoraleatorio:
                self.tentarnovamente = False
                print("Voce acertou")
    
    def pergunta(self):
        self.chute = input("Chute um número:")

    def gerarnumero(self):
        self.valoraleatorio = random.randint(self.valorminimo, self.valormaximo)

Valorchute = ChuteUmNumero()
Valorchute.iniciar()
