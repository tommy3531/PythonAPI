from pprint import pprint
from Controller.ProPublica.Members import Members
from Model.Government.ProPublica.ProPublica_Model import House, Senator, RepDetail
from Controller.Twitter.TwitterController import Twitter
from Controller.UserInput_Controller import Input

""" The ProPublicaManager class managers all classs object from the Controller/ProPublica 
    Controller. """

class ProPublicaManager(object):

    def __init__(self):
        self.member = Members()
        self.twitter = Twitter()
        self.input = Input()

    """ 
    Get the state and House Rep for that state 
    return json of House Reps in list
    """
    def stateHouseRepsDataList(self):

        member = self.member
        state = self.input.setState()
        jsonofHouseReps = member.houseRepsByStateJSON(state)
        parsedHouseJson = self.parseHouse(jsonofHouseReps)
        return parsedHouseJson

    """ 
    Take the json data and create a House Object from the House Model 
    """
    def parseHouse(self, houseJsonData):

        """ Create House Object and store house obj in list """
        houseList = []
        for item in houseJsonData['results']:
            id = item.get("id", "No ID")
            first_name = item.get("first_name", "No First Name")
            middle_name = item.get("middle_name", "No Middle Name")
            last_name = item.get("last_name", "No Last Name")
            name = item.get("name", "No Name")
            party = item.get("party", "No Party")
            role = item.get("role", "No Role")
            twitter_id = item.get("twitter_id", "No Twitter ID")
            faceBook = item.get("facebook_account", "No Facebook Available")
            houseList.append(House(id, first_name, middle_name, last_name, name, party, role, faceBook, twitter_id))
        return houseList

    """ 
    Take the house json data and print out each class attribute
    """
    def printHouse(self, houseJson):
        print("Printing the House Class Attributes stored in HouseList: \n")
        for item in houseJson:
            print("ID          : " + item.id)
            print("First Name  : " + item.firstName)
            print("Middle Name : " + str(item.middleName))
            print("Last Name   : " + item.lastName)
            print("Name        : " + item.name)
            print("Party       : " + item.party)
            print("Role        : " + item.role)
            print("Facebook    : " + str(item.facebook))
            print("TwitterID   : " + str(item.twitterID) + "\n")

    def displayStateHouseRepData(self, houseData):
        self.printHouse(houseData)

    """ 
    Get the state and Senator's for that state 
    return json of Senator in list
    """
    def senatorDataList(self):
        member = self.member
        state = self.input.setState()
        jsonOfSenator = member.sentatorByStateJSON(state)
        parseSenatorJson = self.parseSenator(jsonOfSenator)
        return parseSenatorJson

    """ 
     Take the json data and create a Senator Object from the Senator Model 
     """
    def parseSenator(self, senatorJsonData):

        """ Create Senator Object and store senator obj in list """
        sentatorList = []
        for item in senatorJsonData['results']:
            first_name = item.get("first_name", "No First Name")
            middle_name = item.get("middle_name", "No Middle Name")
            last_name = item.get("last_name", "No Last Name")
            name = item.get("name", "No Name")
            party = item.get("party", "No Party")
            role = item.get("role", "No Role")
            twitter_id = item.get("twitter_id", "No Twitter ID")
            faceBook = item.get("facebook_account", "No Facebook Available")
            sentatorList.append(Senator(first_name, middle_name, last_name, name, party, role, faceBook, twitter_id))
        return sentatorList


    """ 
    Get detail information about a specific politican 
    @ params: Rep ID (Legislative ID)
    """
    def repDetailList(self):
        member = self.member
        repID = self.input.setRepID()
        jsonOfRepDetail = member.repDetailsJSON(repID)
        parseRepDetailJson = self.parseRepDetail(jsonOfRepDetail)
        return parseRepDetailJson

    """ 
     Take the json data and create a RepDetail object from the RepDetail Model 
    """
    def parseRepDetail(self, repDetailJsonData):
        repDetailList = []
        for item in repDetailJsonData['results']:
            crp_id = item.get("crp_id", "No CrpID")
            cspan_id = item.get("cspand_id", "No cspanID")
            google_id = item.get("google_entity_id", "No Google ID")
            govtrack_id = item.get("govtrack_id", "No govtrack ID")
            icpsr_id = item.get("icpsr_id", "No Icpsr ID")
            repDetailList.append(RepDetail(crp_id, cspan_id, google_id, govtrack_id, icpsr_id))
        return repDetailList

    """ 
      Take the repDetai json data and print out each attribute
      @:param RepDetail List
    """

    def printRepDetail(self, detailData):
        print("Printing the Rep Detail from the RepDetail Model: ")
        for item in detailData:
            print("CRPID     : " + str(item.crpID))
            print("CSPANDID  : " + str(item.cspandID))
            print("GOOGLEID  : " + str(item.googleID))
            print("GOVTRACKID: " + str(item.govtrackID))
            print("ICPSRID   : " + str(item.icpsrID) + "\n")

    def displayDetail(self, detailData):
        print("Displays the Reps Detail: ")
        self.printRepDetail(detailData)




    # def getHouseObjectList(self, houseData):
    #
    # def cleanData(self, data):


if __name__ == "__main__":
    i = ProPublicaManager()
    repDetail = i.repDetailList()
    i.displayDetail(repDetail)
    # data = i.stateHouseRepsDataList()
    # i.displayStateHouseRepData(data)


