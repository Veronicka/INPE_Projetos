__author__ = 'Veronica'

class View():

    def start(self):
        print 'EXPERIMENTO ELISA SIMULACAO\n\n'
        return self.menu()

    def menu(self):
        print "1 - Iniciar Simulacao"
        print "2 - Sair"

        return input("\nDigite a opcao: ")

    def portaEscolhida(self, p):
        print "PORTA ESCOLHIDA: "+ p

    def aguardandoPacote(self):
        print "\nEsperando pacote ...\n"

    def portaSemExistencia(self):
        print "PORTA NAO EXISTE\n"

    def semPorta(self):
        print "SEM PORTA\n"

    def finalizar(self):
        print "PROGRAMA FINALIZADO!"

    def opcaoInvalida(self):
        print "NAO EXISTE ESTA OPCAO!\n\n"

    def turnOn(self):
        print "TURN ON"

    def turnOff(self):
        print "TURN OFF"

    def reset(self):
        print "RESET"

    def dataRequest(self):
        print "DATA REQUEST"

    def dataSend(self):
        print "DATA SEND"

    def tempoZero(self):
        print "Mudado o tempo de varredura para 3.2 segundos\n"

    def tempoUm(self):
        print "Mudado o tempo de varredura para 0.8 segundos\n"

    def enviado(self):
        print "ENVIADO"

    def enviando(self):
        print "ENVIANDO"

    def erro(self):
        print "ERRO"

    def geradorIniciando(self):
        print "\nIniciando Gerador de Pacotes\n"

    def pararGerador(self):
        print "Parando Gerador de Pacotes\n"



