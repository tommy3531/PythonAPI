class Senator():
    senator_list = []
    def __init__(self, facebook):
        self.facebook = facebook

    def __str__(self):
        return "Facebook: {}".format(self.facebook)

