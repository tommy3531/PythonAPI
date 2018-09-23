class MenuController():

    def displayStateAndChamberOptions():
        print("""
        1. Search house members by state
        2. Search senate members by state

        4. Exit
        
        """)
        answer = int(input("Please enter a selection: "))
        if (type(answer) == int):
            return answer


    def displayRepOptions():
        print(""" 
        1. Search By RepID
        """)

        answer = int(input("Please enter a selection: "))
        if (type(answer) == int):
            return answer

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
            return numSelection
            # return numSelection


