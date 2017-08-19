class Senator():
    senator_list = []
    def __init__(self, firstName, middleName, lastName, name, party, role, facebook, twitterID):
        self._firstName = firstName
        self._middleName = middleName
        self._lastName = lastName
        self._name = name
        self._party = party
        self._role = role
        self._facebook = facebook
        self._twitterID = twitterID


    # def __str__(self):
    #     return "First Name  : {} \n" \
    #            "Middle Name : {} \n" \
    #            "Last Name   : {} ".format(self._firstName, self._middleName, self._lasName, self._facebook)

