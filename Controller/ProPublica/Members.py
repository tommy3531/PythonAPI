import requests

from Controller.ProPublica.ProPublicaController import ProPublica
from Controller.UserInput_Controller import Input
from Model.ProPublica.ProPublica_House_Model import House
from Model.ProPublica.ProPublica_Senator_Model import Senator


class Members(object):

    def __init__(self):
        self.input = Input()
        self.api = ProPublica()


    def listSentatorByState(self, state):

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

    def listHouseOfRepsByState(self, state):

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

    def repDetails(self, member_id):

        specificMemberURL = "https://api.propublica.org/congress/v1/members"
        url = specificMemberURL + "/" +member_id+ "/votes.json"
        headers = {
            'x-api-key': self.api.key
        }
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            print('Something went wrong'.format(response.status_code))
        else:
            return response.json()


    def getListOfStateSenator(self):
        state = self.input.setState()
        jsonOfStateSentator = self.listSentatorByState(state)
        return jsonOfStateSentator

    def getListOfStateHouseReps(self):
        state = self.input.setState()
        jsonOfHouseReps = self.listHouseOfRepsByState(state)
        return jsonOfHouseReps

    def getRepDetails(self):
        repID = self.input.setRepID()
        jsonOfRepDetails = self.repDetails(repID)
        return jsonOfRepDetails

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


    def parseHouse(self, houseJsonData):

        """ Create House Object and store house obj in list """
        houseList = []
        for item in houseJsonData['results']:
            first_name = item.get("first_name", "No First Name")
            middle_name = item.get("middle_name", "No Middle Name")
            last_name = item.get("last_name", "No Last Name")
            name = item.get("name", "No Name")
            party = item.get("party", "No Party")
            role = item.get("role", "No Role")
            twitter_id = item.get("twitter_id", "No Twitter ID")
            faceBook = item.get("facebook_account", "No Facebook Available")
            houseList.append(House(first_name, middle_name, last_name, name, party, role, faceBook, twitter_id))
        return houseList

    def printHouse(self, houseJson):
        print("Printing the House Class Attributes stored in senatorList: \n")
        for item in houseJson:
            print("First Name  : " + item._firstName)
            print("Middle Name : " + str(item._middleName))
            print("Last Name   : " + item._lastName)
            print("Name        : " + item._name)
            print("Party       : " + item._party)
            print("Role        : " + item._role)
            print("Facebook    : " + str(item._facebook))
            print("TwitterID   : " + str(item._twitterID) + "\n")

    def parseRepDetails(self):
        pass


if __name__ == "__main__":
    member = Members()
    # C001049
    #senator = api.getListOfStateSenator()
    #house = member.getListOfStateHouseReps()
    #parsedSenatorJson = api.parseSenator(senator)
    #api.printSenator(parsedSenatorJson)
    # parsedHouseJson = member.parseHouse(house)
    # print(member.input.repID)
    # print(member.input.chamber)
    # print(member.input.state)
    #member.printHouse(parsedHouseJson)
    #details = api.getRepDetails()
    #billDetails = api.getBillDetails()


