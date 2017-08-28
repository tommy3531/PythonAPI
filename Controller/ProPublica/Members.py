import requests
import pprint
from Controller.ProPublica.ProPublicaController import ProPublica
from Model.Government.ProPublica.ProPublica_Model import House, Senator, RepDetail


class Members(object):

    def __init__(self):
        self.api = ProPublica()


    def sentatorByStateJSON(self, state):

        senatorBaseURL = "https://api.propublica.org/congress/v1/members/senate"
        url = senatorBaseURL + "/" +state+ "/current.json"
        headers = {
            'x-api-key': self.api.key
        }
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            print('Something went wrong'.format(response.status_code))
        else:
            return response.json()

    def houseRepsByStateJSON(self, state):

        houseBaseURL = "https://api.propublica.org/congress/v1/members/house"
        url = houseBaseURL + "/" +state+ "/current.json"
        headers = {
            'x-api-key': self.api.key
        }
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            print('Something went wrong'.format(response.status_code))
        else:
            return response.json()

    def repDetailsJSON(self, member_id):

        specificMemberURL = "https://api.propublica.org/congress/v1/members"
        url = specificMemberURL + "/" +member_id+ ".json"
        headers = {
            'x-api-key': self.api.key
        }
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            print('Something went wrong'.format(response.status_code))
        else:
            return response.json()

        """ 
        Take the json data and create a House Object from the House Model 
        """

    def parseHouse(self, houseJsonData):

        """ Create House Object and store house obj in list """
        houseList = []
        for item in houseJsonData['results']:
            #pprint.pprint(item)
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

    def printSenator(self, senatorJson):
        print("Printing the Senator Class Attributes stored in senatorList: \n")
        for item in senatorJson:
            print("First Name  : " + item._firstName)
            print("Middle Name : " + str(item._middleName))
            print("Last Name   : " + item._lastName)
            print("Name        : " + item._name)
            print("Party       : " + item._party)
            print("Role        : " + item._role)
            print("Facebook    : " + item._facebook)
            print("TwitterID   : " + item._twitterID + "\n")

    def printRepDetail(self, detailData):
        print("Printing the Rep Detail from the RepDetail Model: ")
        for item in detailData:
            print("CRPID     : " + str(item.crpID))
            print("CSPANDID  : " + str(item.cspandID))
            print("GOOGLEID  : " + str(item.googleID))
            print("GOVTRACKID: " + str(item.govtrackID))
            print("ICPSRID   : " + str(item.icpsrID) + "\n")

    # def getListOfStateSenator(self):
    #     state = self.input.setState()
    #     jsonOfStateSentator = self.listSentatorByState(state)
    #     return jsonOfStateSentator

    # def getListOfStateHouseReps(self):
    #     state = self.input.setState()
    #     jsonOfHouseReps = self.houseRepsByStateJSON(state)
    #     return jsonOfHouseReps

    # def getRepDetails(self):
    #     repID = self.input.setRepID()
    #     jsonOfRepDetails = self.repDetails(repID)
    #     return jsonOfRepDetails










    def parseRepDetails(self):
        pass


# if __name__ == "__main__":
    # member = Members()
    # C001049
    #senator = api.getListOfStateSenator()
    # house = member.getListOfStateHouseReps()
    #parsedSenatorJson = api.parseSenator(senator)
    #api.printSenator(parsedSenatorJson)
    # parsedHouseJson = member.parseHouse(house)
    # print(member.input.repID)
    # print(member.input.chamber)
    # print(member.input.state)
    # member.printHouse(parsedHouseJson)
    #details = api.getRepDetails()
    #billDetails = api.getBillDetails()


