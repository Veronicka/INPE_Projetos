__author__ = 'Veronica'

class PacotesGerados():
    def __init__(self):
        self.listaPacotes = []

    def adicionarPacotes(self, pacote):
        self.listaPacotes.append(pacote)

    def getListaPacotes(self):
        temp = []
        for p in self.listaPacotes:
            temp = p
            self.listaPacotes.remove(p)
        return temp

