from Controller.ProPublica_Controller import ProPublica
import pprint

class ProPublicaManager(object):
    def __init__(self):
        self._api = ProPublica()

    def getListOfStateSenator(self):
        jsonOfStateSentator = self._api.listSentatorByState('MO')
        return jsonOfStateSentator

    def getListOfStateHouseReps(self):
        jsonOfHouseReps = self._api.listHouseOfRepsByState('MO')
        return jsonOfHouseReps

    def getRepDetails(self):
        jsonOfRepDetails = self._api.repDetails('C001049')
        return jsonOfRepDetails

    def getBillDetails(self):
        jsonOfBillDetails = self._api.billDetails('115', 'hr2810')
        return jsonOfBillDetails


if __name__ == "__main__":
    api = ProPublicaManager()
    senator = api.getListOfStateSenator()
    house = api.getListOfStateHouseReps()
    details = api.getRepDetails()
    billDetails = api.getBillDetails()
    pprint.pprint(billDetails)
