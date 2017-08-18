from Controller.UserInput_Controller import Input
from Controller.Senator_Controller import Senator
import requests
import pprint


# https://api.propublica.org/congress/v1/members/senate/RI/api-key=FuMVFXTU3fJHtKTHC9v480ZXmampcvt6J0vzYBji/current.json
# https://api.propublica.org/congress/v1/members/senate/MO/api-key=FuMVFXTU3fJHtKTHC9v480ZXmampcvt6J0vzYBji/current.json

class ProPublica(object):
    
    def __init__(self):
        self._key = "FuMVFXTU3fJHtKTHC9v480ZXmampcvt6J0vzYBji"
        self._senatorBaseURL = "https://api.propublica.org/congress/v1/members/senate"
        self._houseBaseURL = "https://api.propublica.org/congress/v1/members/house"
        self._specificMemberURL = "https://api.propublica.org/congress/v1/members"
        self._specificBillURL = "https://api.propublica.org/congress/v1"
        self._input = Input()

    def listSentatorByState(self, state):

        url = self._senatorBaseURL + "/" +state+ "/current.json"
        headers = {
            'x-api-key': self._key
        }
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            print('Something went wrong'.format(response.status_code))
        else:
            return response.json()

    def listHouseOfRepsByState(self, state):

        url = self._houseBaseURL + "/" +state+ "/current.json"
        headers = {
            'x-api-key': self._key
        }
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            print('Something went wrong'.format(response.status_code))
        else:
            return response.json()

    def repDetails(self, member_id):

        url = self._specificMemberURL + "/" +member_id+ "/votes.json"
        headers = {
            'x-api-key': self._key
        }
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            print('Something went wrong'.format(response.status_code))
        else:
            return response.json()

    def billDetails(self, congress, bill_id):
        """ Congress 105-115 """

        url = self._specificBillURL + "/" + congress + "/bills/" + bill_id + ".json"
        headers = {
            'x-api-key': self._key
        }
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            print('Something went wrong'.format(response.status_code))
        else:
            return response.json()

    def getListOfStateSenator(self):
        state = self._input.setState()
        jsonOfStateSentator = self.listSentatorByState(state)
        return jsonOfStateSentator

    def getListOfStateHouseReps(self):
        state = self._input.setState()
        jsonOfHouseReps = self.listHouseOfRepsByState(state)
        return jsonOfHouseReps

    def getRepDetails(self):
        repID = self._input.setRepID()
        jsonOfRepDetails = self.repDetails(repID)
        return jsonOfRepDetails

    def getBillDetails(self):
        jsonOfBillDetails = self.billDetails('115', 'hr2810')
        return jsonOfBillDetails

    def parseSenator(self, senatorJsonData):

        """ Need to create a senator Class to create a senator OBJ """
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


    def parseHouse(self):
        pass

    def parseRepDetails(self):
        pass


if __name__ == "__main__":
    api = ProPublica()
    # C001049
    senator = api.getListOfStateSenator()
   # house = api.getListOfStateHouseReps()
   # details = api.getRepDetails()
    #billDetails = api.getBillDetails()
    print("This is from the ProPublica Controller: ")
    # Returns a senator obj
    parsedSenatorJson = api.parseSenator(senator)
    # Print out the senator obj attributes
    api.printSenator(parsedSenatorJson)
