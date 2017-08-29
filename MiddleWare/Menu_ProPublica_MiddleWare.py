from Manager.Menu_Manager import MenuManager
from Manager.ProPublica_Manager import ProPublicaManager


class MenuProPublicMiddleWare():

    def __init__(self):
        self.menuManager = MenuManager()
        self.ProPublicaManager = ProPublicaManager()

    def stateAndChamberMenu(self):
        print("From MiddleWare: ")
        selection = self.menuManager.searchByStateAndChamber()
        #print("This is the middleware selection: " + str(selection))
        return selection

    def repIDMenu(self):
        selection = self.menuManager.searchByRepID()
        return selection

    def selectHouseOrSenateMethod(self, number):
        if number == 1:
            print("Search house members by state: ")
            self.ProPublicaManager.houseDataList()
        elif (number == 2):
            print("Search senate members by state: ")
            self.ProPublicaManager.senatorDataList()

        else:
            print("You entered something fucked up: " + str(number))
            #self.startMenu()

    def selectRep(self, number):
        if(number == 1):
            print("Search for specific political leader by repID: ")
            self.ProPublicaManager.repDetailList()

if __name__ == "__main__":
    i = MenuProPublicMiddleWare()
    selectionValue = i.stateAndChamberMenu()
    #print("This is the selectionValue: " + selectionValue)
    i.selectHouseOrSenateMethod(selectionValue)

    repSelection = i.repIDMenu()
    i.selectRep(repSelection)
