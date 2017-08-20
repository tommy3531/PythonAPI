from Controller.ProPublica.Members import Members

class ProPublicaManager(object):

    def __init__(self):
        self.member = Members()

    def g(self):
        a = self.member.input.ge
