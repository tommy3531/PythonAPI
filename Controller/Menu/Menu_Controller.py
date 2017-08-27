class MenuController():

    def displayMenuOptions(self):
        print("""
        1. Search by State
        2. Search by State within Chamber(State or House)
        3. Exit
        
        """)
        answer = input("Please enter a selection: ")
        return int(answer)

    def checkIfNum(self, numSelection):
        if type(numSelection) == int:
            print("Number is valid: " + str(numSelection))
            return numSelection

        else:
            print("The input is not a valid number: " + numSelection)
            #self.displayMenuOptions()

    """ THis is messed up"""
    def checkIfNumIsInRange(self, numSelection):
        if numSelection in range(1,3):
            number = numSelection

            return number
        else:
            print("Number is not in range of 1,3: " + str(numSelection))
            self.rerun()
            # return numSelection
    def rerun(self):
        selection = self.displayMenuOptions()
        isNumber = self.checkIfNum(selection)
        validRange = self.checkIfNumIsInRange(isNumber)
        return validRange

