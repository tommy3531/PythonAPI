class Senator:

    def __init__(self, firstName, middleName, lastName, name, party, role, facebook, twitterID):
        self._firstName = firstName
        self._middleName = middleName
        self._lastName = lastName
        self._name = name
        self._party = party
        self._role = role
        self._facebook = facebook
        self._twitterID = twitterID


class House:

    def __init__(self, id, firstName, middleName, lastName, name, party, role, facebook, twitterID):
        self.id = id
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.name = name
        self.party = party
        self.role = role
        self.facebook = facebook
        self.twitterID = twitterID


class RepDetail:
    def __init__(self, crpID, cspanID, googleID, govtrackID, icpsrID):
        self.crpID = crpID
        self.cspandID = cspanID
        self.googleID = googleID
        self.govtrackID = govtrackID
        self.icpsrID = icpsrID
