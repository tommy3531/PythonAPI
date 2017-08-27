class MenuController():

    def displayMenuOptions(self):
        print("""
        1. Search by State
        2. Search by State within Chamber(State or House)
        3. Exit
        
        """)
        answer = int(input("Please enter a selection: "))
        if (type(answer) == int):
            return answer
        else:
            self.displayMenuOptions()

    def checkIfNum(self, numSelection):
        if type(numSelection) == int:
            print("Number is valid: " + str(numSelection))
            return numSelection

        else:
            print("The input is not a valid number: " + numSelection)
            #self.displayMenuOptions()

    def checkIfNumIsInRange(self, numSelection):
        if numSelection in range(0,4):
            return numSelection
        else:
            print("Number is not in range of 1,3: " + str(numSelection))
            return False
            # return numSelection


