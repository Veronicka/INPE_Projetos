__author__ = 'Veronica'

from src.model.frameGenerator import GeradorPacote
from src.model.generatedFrames import PacotesGerados
from src.model.frameSend import EnviarPacote
from src.model.frameListener import RecebedorPacote
from src.controller.controller import Controller

class ExperimentoElisa(object):

    def __init__(self, dispositivo):
        self.__dispositivo = dispositivo
        self.__enviarPacote = EnviarPacote(self.__dispositivo)
        self.__pacotesGerados = PacotesGerados()
        self.__geradorPacote = GeradorPacote(self.__pacotesGerados)
        self.__controller = Controller()

    def transformador(self, pacote):
        f = ''
        for i in pacote:
            f += i
        respostaOBC = [ord(b) for b in f]
        if len(respostaOBC) > 1:
            print respostaOBC
            self.pacotesRecebidos(respostaOBC)

    def pacotesRecebidos(self, respostaOBC):

        if respostaOBC[2] == 11:
            self.__controller.visualizar().turnOn()
            self.__enviarPacote.enviar(self.__geradorPacote.acknowledge())
            self.__geradorPacote.iniciarThread()
            self.__controller.visualizar().geradorIniciando()

        elif respostaOBC[2] == 1:
            self.__controller.visualizar().dataRequest()
            a = self.__pacotesGerados.getListaPacotes()
            self.__enviarPacote.enviar(a)
            print a

        elif respostaOBC[2] == 2:
            self.__controller.visualizar().dataSend()

            self.__enviarPacote.enviar(self.__geradorPacote.acknowledge())
            if respostaOBC[4] == 0:
                self.__controller.visualizar().tempoZero()
                self.__geradorPacote.mudarTempo(0x0)
            else:
                self.__controller.visualizar().tempoUm()
                self.__geradorPacote.mudarTempo(0x1)

        elif respostaOBC[2] == 7:
            self.__controller.visualizar().reset()
            self.__enviarPacote.enviar(self.__geradorPacote.acknowledge())
            self.__geradorPacote.varredura = 0x0
            self.__geradorPacote.mudarTempo(0x0)
            self.__pacotesGerados.listaPacotes = []

        elif respostaOBC[2] == 9:
            self.__controller.visualizar().turnOff()
            self.__enviarPacote.enviar(self.__geradorPacote.acknowledge())
            self.__geradorPacote.terminarThread()
            RecebedorPacote(self.__dispositivo).terminarThread()

        else:
            self.__controller.visualizar().erro()

