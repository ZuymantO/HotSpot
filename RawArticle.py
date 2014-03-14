#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wikipedia as wiki
from pymongo import MongoClient

class RawArticle:

    def __init__(self, wiki):
        self.raw      = wiki
        self.ligth     = ""

    def getRaw():
        return self.raw

    def getLight():
        return self.light
    
    def process():
        self.light = self.raw
        return self.raw # Stop word process



