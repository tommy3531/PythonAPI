import re
from Controller.ProPublica.Members import Members
from Controller.Twitter.TwitterController import Twitter
from Controller.UserInput_Controller import Input

""" The ProPublicaManager class managers all classs object from the Controller/ProPublica 
    Controller. """

class ProPublicaManager(object):

    def __init__(self):
        self.member = Members()
        self.twitter = Twitter()
        self.input = Input()

    def displayStateHouseRepData(self, houseData):
        member = self.member
        member.printHouse(houseData)

    """ 
    Get the state and House Rep for that state 
    return json of House Reps in list
    """
    def stateHouseRepsDataList(self):
        member = self.member
        state = self.input.setState()
        jsonofHouseReps = member.houseRepsByStateJSON(state)
        parsedHouseJson = member.parseHouse(jsonofHouseReps)
        # member.printHouse(parsedHouseJson)
        return parsedHouseJson

    """ 
    Get the state and House Rep for that state 
    return json of House Reps in list
    """
    def senatorDataList(self):
        member = self.member
        state = self.input.setState()
        jsonOfSenator = member.sentatorByStateJSON(state)
        parseSenatorJson = member.parseSenator(jsonOfSenator)
        return parseSenatorJson



    # def getHouseObjectList(self, houseData):
    #
    # def cleanData(self, data):


if __name__ == "__main__":
    i = ProPublicaManager()
    data = i.stateHouseRepsDataList()
    i.displayStateHouseRepData(data)


