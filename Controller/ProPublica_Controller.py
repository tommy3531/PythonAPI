import requests

# https://api.propublica.org/congress/v1/members/senate/RI/api-key=FuMVFXTU3fJHtKTHC9v480ZXmampcvt6J0vzYBji/current.json
# https://api.propublica.org/congress/v1/members/senate/MO/api-key=FuMVFXTU3fJHtKTHC9v480ZXmampcvt6J0vzYBji/current.json

class ProPublica(object):
    
    def __init__(self):
        self._key = "FuMVFXTU3fJHtKTHC9v480ZXmampcvt6J0vzYBji"
        self._senatorBaseURL = "https://api.propublica.org/congress/v1/members/senate"
        self._houseBaseURL = "https://api.propublica.org/congress/v1/members/house"
        self._specificMemberURL = "https://api.propublica.org/congress/v1/members"
        self._specificBillURL = "https://api.propublica.org/congress/v1"

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