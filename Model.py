#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wikipedia
import tfidf
from pymongo import MongoClient
client = MongoClient()
db = client.test_database
articles = db.articles


