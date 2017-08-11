import json
import pprint
from Controller.News_API_Controller import listSources
from Model.Media import News_Model
from Controller.News_API_Controller import listSourceByCategory
from Controller.News_API_Controller import listArticleFromSource

def listSourcesJson():

    # The respose is stored in JsonListSource
    jsonListSources = listSources()
    jsonResponse = json.loads(jsonListSources)
    print(type(jsonResponse))






if __name__ == "__main__":
    print("This is from listSourceJson: ")
    print(listSourcesJson())

