__author__ = 'Veronica'

from threading import Thread
from src.controller.controller import Controller

class RecebedorPacote():
    def __init__(self, dispositivo):
        self.__dispositivo = dispositivo
        self.__controller = Controller()
        self.__lista = []
        self.__ok = True

    def iniciarThread(self):
        self.__controller.visualizar().aguardandoPacote()
        try:
            t1 = Thread(target=self.receberPacote)
            t1.start()
        except Exception as e:
            print e

    def terminarThread(self):
        self.__controller.visualizar().pararGerador()
        self.__ok = False

    def getLista(self):
        temp = self.__lista
        self.__lista = []
        return temp

    def receberPacote(self):
        while self.__ok:
            try:
                data = self.__dispositivo.ouvirPorta()
                if len(data) > 0:
                    self.__lista.append(data)
            except Exception:
                self.__controller.visualizar().erro()

