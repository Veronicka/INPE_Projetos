__author__ = 'Veronica'

class Pacote():
    def __init__(self, conteudo):
        self.__header = [0xeb, 0x95, 0x4]
        self.__conteudo = conteudo
        self.__checksum = self.getChecksum()

    def getChecksum(self):
        frame = self.__header + self.__conteudo
        return sum(frame[11:]) & 0xFF

    def getPacote(self):
        self.__header.append(len(self.__conteudo[11:]))
        f = self.__header + self.__conteudo
        f.append(self.__checksum)
        return f


