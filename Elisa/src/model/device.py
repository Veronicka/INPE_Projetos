__author__ = 'Veronica'

from serial import Serial, SerialException
from src.controller.controller import Controller
import sys

class Dispositivo():
    def __init__(self):
        self.controller = Controller()
        self.porta = self.escolhaPorta()

    def escolhaPorta(self):
        MAX_PORTAS = 10 # numero maximo de portas
        k = 1

        #configuracao da porta
        baudrate = 9600
        bytesize = 8
        parity = 'N'
        stopbits = 1
        timeout = 0
        #controle de fluxo
        xonxoff = False
        rtscts = False

        dict = {}
        for p in ['COM%s' % (i + 1) for i in range(MAX_PORTAS)]:
            try:
                s = Serial(p)
                dict[k] = s.portstr
                k+=1
                s.close()
            except (OSError, SerialException):
                pass
        for i in dict:
            print i, " - ", dict[i]

        p = 15
        if len(dict) == 0:
            self.controller.visualizar().semPorta()
            sys.exit(0)
        else:
            while(p not in dict):
                p = int(input("\nEscolha a porta serial: "))
                if p <= len(dict) and p!=0:
                    try:
                        self.porta = Serial(dict[p], baudrate, bytesize, parity, stopbits, timeout, xonxoff, rtscts)
                        self.controller.visualizar().portaEscolhida(self.porta.portstr)
                        return self.porta
                    except SerialException:
                        self.controller.visualizar().erro()
                        sys.exit(0)
                else:
                    self.controller.visualizar().portaSemExistencia()

    def ouvirPorta(self):
        return self.porta.read(256)

    def escreverPorta(self, pacote):
        return self.porta.write(pacote)

                
   


