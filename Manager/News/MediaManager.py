from Controller.News_API_Controller import listSources
from Model.Media.News_Model import NewsData

newsList = []

def listSourcesJson():

    # The respose is stored in JsonListSource
    jsonListSources = listSources()

    # print(jsonListSources['sources'])
    for item in jsonListSources['sources']:
        id = item.get("id", "No ID Available")
        name = item.get("name", "No ID Available")
        description = item.get("description", "No Description")
        #print(id)
        #print(name)
        #print(description)
        newsList.append(NewsData(description, name, id))

    return newsList

def getNewsList():
    for obj in newsList:
        print("\nThis is the id: " + obj._id)
        print("\nThis is the name: " + obj._name)
        print("\nThis is the description: " + obj._description)

    return newsList

def printOut():
    classList = listSourcesJson()
    # for obj in classList:
    #     print("\nThis is the id: " + obj._id)
    #     print("\nThis is the name: " + obj._name)
    #     print("\nThis is the description: " + obj._description)



