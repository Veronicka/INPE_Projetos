__author__ = 'Veronica'

from threading import Thread
from frame import Pacote
from time import sleep

class GeradorPacote():
    def __init__ (self, pacotesGerados):
        self.varredura = 0x0
        self.__pacotesGerados = pacotesGerados
        self.__ok = True
        self.__tempo = 0x0

    def iniciarThread(self):
        t1 = Thread(target=self.enviarPacotes)
        t1.start()

    def mudarTempo(self, tempo):
        self.__tempo = tempo

    def terminarThread(self):
        self.__ok = False

    def acknowledge(self):
        ack = [0xeb, 0x95, 0x3, 0x0, 0x55, 0xAA]
        return ack


    def criarModoNormal(self, v, t):
        modoNormal = [0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, t, v, 0x7F, 0x65, 0x51, 0x40, 0x33, 0x29, 0x21, 0x1A, 0x15,
                      0x10, 0xD, 0xA, 0x8, 0x7, 0x5, 0x4, 0xFE, 0xCA, 0xA1, 0x81, 0x66, 0x52, 0x41, 0x34, 0x29, 0x21,
                      0x1A, 0x15, 0x11, 0xD, 0xB, 0x8, t, v, 0x7F, 0x65, 0x51, 0x40, 0x33, 0x29, 0x21, 0x1A, 0x15,
                      0x10, 0xD, 0xA, 0x8, 0x7, 0x5, 0x4, 0xFE, 0xCA, 0xA1, 0x81, 0x66, 0x52, 0x41, 0x34, 0x29, 0x21,
                      0x1A, 0x15, 0x11, 0xD, 0xB, 0x8]

        return Pacote(modoNormal).getPacote()

    def criarModoNormal2(self, v, t):
        modoNormal = [0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, t, v, 0x7F, 0x65, 0x51, 0x40, 0x33, 0x29, 0x21, 0x1A, 0x15,
                      0x10, 0xD, 0xA, 0x8, 0x7, 0x5, 0x4, 0xFE, 0xCA, 0xA1, 0x81, 0x66, 0x52, 0x41, 0x34, 0x29, 0x21,
                      0x1A, 0x15, 0x11, 0xD, 0xB, 0x8]

        return Pacote(modoNormal).getPacote()

    def criarHousekeeping(self, v, t):
        hkp = [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, t, 0x75, 0x7F, 0x65, 0x51, 0x40, 0x33, 0x29, 0x21, 0x1A, 0x15,
               0x10, 0xD, 0xA, 0x8, 0x7, 0x5, 0x4, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64,
               0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64, 0x64,
               0x64, 0x64, 0x64, 0x64, t, v, 0x7F, 0x65, 0x51, 0x40, 0x33, 0x29, 0x21, 0x1A, 0x15, 0x10,
               0xD, 0xA, 0x8, 0x7, 0x5, 0x4, 0xFE, 0xCA, 0xA1, 0x81, 0x66, 0x52, 0x41, 0x34, 0x29, 0x21, 0x1A, 0x15,
               0x11, 0xD, 0xB, 0x8]

        return Pacote(hkp).getPacote()

    def enviarPacotes(self):
        t = 0x0
        while self.__ok:
            if t == 0:
                if self.varredura >= 200 or self.varredura == 0:
                    # housekeeping
                    sleep(6.4) # 2 * 0.8, pois e o tempo de cada varredura
                    t = self.__tempo

                    #pacote com o housekeeping e uma varredura
                    self.varredura = 0x0 #caso a varredura seja igual a 200 ela e zerada
                    self.__pacotesGerados.adicionarPacotes(self.criarHousekeeping(self.varredura, t))
                    self.varredura = 197

                    if t != 0:
                        self.varredura = 0

                else:
                    # modo normal

                    # pacote com 2 varreduas
                    sleep(6.4)
                    self.__pacotesGerados.adicionarPacotes(self.criarModoNormal(self.varredura, t))

                    self.varredura += 0x1
                    #pacote com 2 varreduras
                    sleep(6.4)
                    self.__pacotesGerados.adicionarPacotes(self.criarModoNormal(self.varredura, t))

                    self.varredura += 0x1
                    #pacote com 1 varredura
                    sleep(3.2)
                    self.__pacotesGerados.adicionarPacotes(self.criarModoNormal2(self.varredura, t))
                    self.varredura += 0x1

            else:
                if self.varredura >= 800 or self.varredura == 0:
                    # housekeeping
                    sleep(1.6)  # 2 * 1.6, pois e o tempo de cada varredura
                    t = self.__tempo

                    # pacote com o housekeeping e uma varredura
                    self.varredura = 0x0  # caso a varredura seja igual a 800 ela e zerada
                    self.__pacotesGerados.adicionarPacotes(self.criarHousekeeping(self.varredura, t))
                    self.varredura = 0x1

                    if t != 1:
                        self.varredura = 0

                else:
                    # modo normal
                    # 5 pacotes com 2 varreduras cada
                    for i in range(0,4):
                        sleep(1.6) #2* 0.8, pois e o tempo de cada varredura
                        self.__pacotesGerados.adicionarPacotes(self.criarModoNormal(self.varredura, t))
                        self.varredura += 0x1







