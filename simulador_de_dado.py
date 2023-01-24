#ProjetoPython
#Simulador de dado


import random

#import PySimpleGUI

class SimuladorDado:
    def __init__(self):
        self.valorminimo = 1
        self.valormaximo = 6
    
    def iniciar(self):
        resposta = input("Deseja rodar o dado?")
        if resposta == "sim":
            self.GerarValorDado()
        elif resposta == "nao":
            print("OK")
        else:
            print("Pfvr digitar sim ou não")

    def GerarValorDado(self):
        print(random.randint(self.valorminimo,self.valormaximo))

simulador = SimuladorDado()
simulador.iniciar() 
