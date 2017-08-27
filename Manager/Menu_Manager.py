from Controller.Menu.Menu_Controller import MenuController

class MenuManager():

    def __init__(self):
        self.menu = MenuController()

    def displayMenu(self):
        selection = self.menu.displayMenuOptions()
        return selection

    def checkSelectionIsVALID(self, input):
        print("This is the MenuManager: ")
        checkNumStatus = self.menu.checkIfNum(input)
        return checkNumStatus

    def checkSelectionRange(self, input):
        rangeSelection = self.menu.checkIfNumIsInRange(input)
        print(rangeSelection)


if __name__ == "__main__":
    i = MenuManager()
    selectionInput = i.displayMenu()
    isValid = i.checkSelectionIsVALID(selectionInput)
    i.checkSelectionRange(isValid)

