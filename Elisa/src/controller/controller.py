from src.view.view import View

class Controller():
    def __init__(self):
        self.__view = View()

    def visualizar(self):
        return self.__view
