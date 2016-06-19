from threading import Thread
from time import sleep
from src.model.device import Dispositivo
from src.model.elisaExperiment import ExperimentoElisa
from src.model.frameListener import RecebedorPacote
from src.view.view import View

class Integrador():

    def __init__(self):
        self.__dispositivo = None
        self.__elisa = None
        self.__recebedorPacote = None
        self.__view = View()
        self.start(self.__view.start())

    def start(self, opcao):
        if opcao == 1:
            self.__dispositivo = Dispositivo()
            self.__elisa = ExperimentoElisa(self.__dispositivo)
            self.__recebedorPacote = RecebedorPacote(self.__dispositivo)
            self.__recebedorPacote.iniciarThread()
            self.receber()
            self.ler()

        elif opcao == 2:
            return self.__view.finalizar()

        else:
            self.__view.opcaoInvalida()
            return self.start(self.__view.start())

    def receber(self):
        t = Thread(target=self.ler)
        t.start()

    def ler(self):
        while True:
            sleep(1)
            self.__elisa.transformador(self.__recebedorPacote.getLista())








