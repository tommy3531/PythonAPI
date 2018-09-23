class Input():
    # chamber = ""
    # repId = ""
    # state = ""
    #
    # def listUserInput(self):
    #     listAttributes = "Chamber = %s repID = %s state = %s" % (self.chamber, self.repId, self.state)
    #     return listAttributes
    def __init__(self):
        self.chamber = None
        self.repID = None
        self.state = None

    def setChamber(self):
        userChamber = input("Enter Chamber (House or Senate): ")

        self.chamber = userChamber
        return self.chamber

    def setRepID(self):
        userRepID = input("Enter the representative ID: ")
        self.repID = userRepID
        return self.repID

    def setState(self):
        userState = input("Enter Two Digit State (MO): ")
        self.state = userState
        return self.state

    def getchamber(self):
        return self.chamber

    def getRepID(self):
        return self.repID

    def getState(self):
        return self.state
