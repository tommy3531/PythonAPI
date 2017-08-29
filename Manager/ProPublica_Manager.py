from pprint import pprint
from Controller.ProPublica.Members import Members
from Controller.UserInput_Controller import Input

""" The ProPublicaManager class managers all classs object from the Controller/ProPublica 
    Controller. """

class ProPublicaManager(object):

    def __init__(self):
        self.member = Members()
        self.input = Input()

    """ 
    Get the state and House Rep for that state 
    return json of House Reps in list
    """
    def houseDataList(self):

        member = self.member
        state = self.input.setState()
        jsonofHouseReps = member.houseRepsByStateJSON(state)
        parsedHouseJson = member.parseHouse(jsonofHouseReps)
        member.printHouse(parsedHouseJson)
        """ Returns list of House objects"""
        # for i in parsedHouseJson:
        #     print(i.id)
        #return parsedHouseJson

    """ 
    Get the state and Senator's for that state 
    return json of Senator in list
    """
    def senatorDataList(self):
        member = self.member
        state = self.input.setState()
        jsonOfSenator = member.sentatorByStateJSON(state)
        parseSenatorJson = member.parseSenator(jsonOfSenator)
        member.printSenator(parseSenatorJson)
        return parseSenatorJson

    """ 
    Get detail information about a specific politican 
    @ params: Rep ID (Legislative ID)
    """
    def repDetailList(self):
        member = self.member
        repID = self.input.setRepID()
        jsonOfRepDetail = member.repDetailsJSON(repID)
        parseRepDetailJson = member.parseRepDetail(jsonOfRepDetail)
        member.printRepDetail(parseRepDetailJson)
        return parseRepDetailJson

    def displayStateHouseRepData(self, houseData):
        for item in houseData:
            print(item.id)

    """ 
      Take the repDetai json data and print out each attribute
      @:param RepDetail List
    """

    def displayDetail(self, detailData):
        print("Displays the Reps Detail: ")
        self.printRepDetail(detailData)


# if __name__ == "__main__":
#     i = ProPublicaManager()
#     houseDataList = i.houseDataList()
#     for item in houseDataList:
#         print(item.id)
    # data = i.stateHouseRepsDataList()
    # i.displayStateHouseRepData(data)


