class MenuController():

    def displayMenuOptions(self):
        print("""
        1. Search house members by state
        2. Search senate members by state
        3. Search for specific political leader by repID
        4. Exit
        
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
            return numSelection
            # return numSelection


