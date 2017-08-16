import requests


def getAllSources():
    return 'https://newsapi.org/v1/sources?apiKey=e1c234eb02844c84a10860a43701cce8'

def getSourcesByCategory(category):
    return 'https://newsapi.org/v1/sources?apiKey=e1c234eb02844c84a10860a43701cce8&category=' + category

def getArticleFromSource(source):
    return 'https://newsapi.org/v1/articles?source=' + source +'&sortBy=top&apiKey=e1c234eb02844c84a10860a43701cce8'


def listSources():
    resp = requests.get(getAllSources())
    if resp.status_code != 200:
        print('Something went wrong'.format(resp.status_code))
    else:
        # print("This is the json")
        return resp.json()


def listSourceByCategory():
    return requests.get(getSourcesByCategory('general'))

def listArticleFromSource():
    return requests.get(getArticleFromSource('bbc-news'))

