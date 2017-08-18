# from Controller.ProPublica_Controller import ProPublica
# from Controller.UserInput_Controller import Input
# import pprint
#
# class ProPublicaManager(object):
#     def __init__(self):
#         self._api = ProPublica()
#         self._input = Input()
#
#     def getListOfStateSenator(self):
#         state = self._input.setState()
#         jsonOfStateSentator = self._api.listSentatorByState(state)
#         return jsonOfStateSentator
#
#     def getListOfStateHouseReps(self):
#         state = self._input.setState()
#         jsonOfHouseReps = self._api.listHouseOfRepsByState(state)
#         return jsonOfHouseReps
#
#     def getRepDetails(self):
#         repID = self._input.setRepID()
#         jsonOfRepDetails = self._api.repDetails(repID)
#         return jsonOfRepDetails
#
#     def getBillDetails(self):
#         jsonOfBillDetails = self._api.billDetails('115', 'hr2810')
#         return jsonOfBillDetails
#
#
# if __name__ == "__main__":
#     api = ProPublicaManager()
#     # C001049
#     senator = api.getListOfStateSenator()
#     house = api.getListOfStateHouseReps()
#     details = api.getRepDetails()
#     billDetails = api.getBillDetails()
#     pprint.pprint(senator)
