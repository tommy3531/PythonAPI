import requests

from Controller.ProPublica.ProPublicaController import ProPublica


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


    # def getListOfStateSenator(self):
    #     state = self.input.setState()
    #     jsonOfStateSentator = self.listSentatorByState(state)
    #     return jsonOfStateSentator

    # def getListOfStateHouseReps(self):
    #     state = self.input.setState()
    #     jsonOfHouseReps = self.houseRepsByStateJSON(state)
    #     return jsonOfHouseReps

    def getRepDetails(self):
        repID = self.input.setRepID()
        jsonOfRepDetails = self.repDetails(repID)
        return jsonOfRepDetails



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


