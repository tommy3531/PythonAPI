class User():

    def __init__(self, chamber, repID, state):
        self._chamber = chamber
        self._state = state
        self._repID = repID


if __name__ == "__main__":
    chamber = input("Enter Chamber (House or Senate): ")
    repID = input("Enter the representative ID: ")
    userState = input("Enter Two Digit State (MO): ")
    userData = User(chamber, repID, userState)
    print("This is the state: " + str(userData._state))
    print("This is the chamber: " + str(userData._chamber))
    print("This is the repID: " + str(userData._repID))