from Controller.Menu.Menu_Controller import MenuController

class MenuManager():

    def __init__(self):
        self.menu = MenuController()

    def searchByStateAndChamber(self):
        selection = self.menu.displayStateAndChamberOptions()
        isNumber = self.menu.checkIfNum(selection)
        isRange = self.menu.checkIfNumIsInRange(isNumber)
        return isRange

    def searchByRepID(self):
        selection = self.menu.displayRepOptions()
        isNumber = self.menu.checkIfNum(selection)
        isRange = self.menu.checkIfNumIsInRange(isNumber)
        return isRange





# if __name__ == "__main__":
#     i = MenuManager()
#     i.start()
#     # selectionInput = i.displayMenu()
#     # isValid = i.checkSelectionIsVALID(selectionInput)
#     # i.checkSelectionRange(isValid)
#     # print(rangeValid)

