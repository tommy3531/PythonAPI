# https://newsapi.org/v1/sources
# List of New Sources
# https://newsapi.org/v1/sources?apiKey= e1c234eb02844c84a10860a43701cce8
# https://newsapi.org/v1/sources?apiKey= e1c234eb02844c84a10860a43701cce8&category=general
import json

class NewsData:

    def __init__(self, description, name, id):
        self._description = description
        self._name = name
        self._id = id

    def name(self):
        return self._name
    def description(self):
        return self._description
    def id(self):
        return self._id

