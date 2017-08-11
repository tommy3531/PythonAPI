# https://newsapi.org/v1/sources
# List of New Sources
# https://newsapi.org/v1/sources?apiKey= e1c234eb02844c84a10860a43701cce8
# https://newsapi.org/v1/sources?apiKey= e1c234eb02844c84a10860a43701cce8&category=general
import json

class News_Model(object):
    def __init__(self, category, country, description, name, url, id):
        self.category = category
        self.country = country
        self.description = description
        self.name = name
        self.url = url
        self.id = id

