from src.controller.controller import Controller

class EnviarPacote():
    def __init__(self, dispositivo):
        self.__controller = Controller()
        self.__dispositivo = dispositivo

    def enviar(self, pacote):
        try:
            self.__dispositivo.escreverPorta(pacote)
            self.__controller.visualizar().enviado()

        except Exception:
            self.__controller.visualizar().erro()