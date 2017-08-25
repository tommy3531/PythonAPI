from Controller.ProPublica.Members import Members
from Controller.Twitter.TwitterController import Twitter

class ProPublicaManager(object):

    def __init__(self):
        self.member = Members()
        self.twitter = Twitter()

    def stateHouseRepsData(self):
        member = Members()
        house = member.getListOfStateHouseReps()
        parsedHouseJson = member.parseHouse(house)
        member.printHouse(parsedHouseJson)
        return parsedHouseJson


if __name__ == "__main__":
    i = ProPublicaManager()
    i.stateHouseRepsData()
