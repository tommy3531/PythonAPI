from Controller.ProPublica_Controller import listSentatorByState

def getSources():
    s = listSentatorByState('MO')
    print("This is from the manager: ")
    print(s)


if __name__ == "__main__":
    getSources()