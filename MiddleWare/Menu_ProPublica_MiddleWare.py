from Manager.Menu_Manager import MenuManager
from Manager.ProPublica_Manager import ProPublicaManager


class MenuProPublicMiddleWare():

    def __init__(self):
        self.menuManager = MenuManager()
        self.ProPublicaManager = ProPublicaManager()

    def startMenu(self):
        print("From MiddleWare: ")
        selection = self.menuManager.start()
        #print("This is the middleware selection: " + str(selection))
        return selection

    def selectStartMethod(self, number):
        if number == 1:
            print("Search house members by state: ")
            self.ProPublicaManager.houseDataList()
        elif (number == 2):
            print("Search senate members by state: ")
            self.ProPublicaManager.senatorDataList()
        elif(number == 3):
            print("Search for specific political leader by repID: ")
            self.ProPublicaManager.repDetailList()
        else:
            print("You entered something fucked up: " + str(number))
            #self.startMenu()

if __name__ == "__main__":
    i = MenuProPublicMiddleWare()
    selectionValue = i.startMenu()
    #print("This is the selectionValue: " + selectionValue)
    i.selectStartMethod(selectionValue)
