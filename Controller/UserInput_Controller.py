class Input(object):

    def __init__(self):
        self._chamber = None
        self._repID = None
        self._state = None

    def setChamber(self):
        chamber = input("Enter Chamber (House or Senate): ")
        self._chamber = chamber
        return self._chamber

    def setRepID(self):
        repID = input("Enter the representative ID: ")
        self._repID = repID
        return self._repID

    def setState(self):
        userState = input("Enter Two Digit State (MO): ")
        self._state = userState
        return self._state
