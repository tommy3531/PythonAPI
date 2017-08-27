from Manager.Menu_Manager import MenuManager
from Manager.ProPublica_Manager import ProPublicaManager

class MenuProPublicMiddleWare():

    def __init__(self):
        self.menuManager = MenuManager()

    def menuSelection(self):
        print("From MiddleWare: ")
        selectionNum = self.menuManager.checkIfSelectionIsInt()
        booleanCheck = self.menuManager.checkSelectionRange(selectionNum)
        print(booleanCheck)
        # return selectionNum


# if __name__ == "__main__":
#     i = MenuProPublicMiddleWare()
#     i.menuSelection()
