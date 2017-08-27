from Controller.Menu.Menu_Controller import MenuController

class MenuManager():

    def __init__(self):
        self.menu = MenuController()

    def start(self):
        selection = self.menu.displayMenuOptions()
        isNumber = self.menu.checkIfNum(selection)
        booleanValue = self.menu.checkIfNumIsInRange(isNumber)
        if booleanValue == False:
            print("Is the input in the correct range: " + str(booleanValue))
            self.start()
        else:
            print("Input is a number and within the correct range: " + str(booleanValue))





if __name__ == "__main__":
    i = MenuManager()
    i.start()
    # selectionInput = i.displayMenu()
    # isValid = i.checkSelectionIsVALID(selectionInput)
    # i.checkSelectionRange(isValid)
    # print(rangeValid)

