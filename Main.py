#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import pymongo
import string
import math
import time
import wikipedia
from textblob import TextBlob as tb
import Model as md
import TfIdf as tf
import Advise as ad
import Article as art
import bson

import threading
import thread

stop_words=["le","la","les","un","une","de","des","en","du","l'","mais","ou","et","donc","or","ni","car","ces","ce","sa","mon","ton","son","leur","leurs","je","tu","il","elle","on","nous","vous","ils","elles"
            ,"mes","tes","nos","vos",
            "Le","La","Les","Un","Une","De","Des","En","Du","L'","Mais","Ou","Et","Donc","Or","Ni","Car","Ces","Ce","Sa","Mon","Ton","Son","Leur","Leurs","Je","Tu","Il","Elle","On","Nous","Vous","Ils","Elles"
            ,"Mes","Tes","Nos","Vos"]


"""
def tf(word, blob):
    if word in stop_words:
        return 0.0
    x = blob.words.count(word)
    y = len(blob.words)
    #print x
    #print y
    return x/(y*1.0)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    x =float(1+ len(bloblist) / (1 + n_containing(word, bloblist)))
    return math.log(x)
    #print x
    #try :
    #    y = math.log(x)
    #except ValueError:
    #    y = 0
    #return y

def tfidf(word, blob, bloblist):
    x = tf(word, blob) 
    y = idf(word, bloblist)
    #print x
    #print y
    return x*y
"""
wikipedia.set_lang("fr")
"""
titles = wikipedia.random(pages=10)

def page(titles):
    db = []
    for i in range(len(titles)):
        try :
            db.append(wikipedia.WikipediaPage(titles[i]))
        except wikipedia.exceptions.DisambiguationError :
            #print type(inst)
            #print inst.args
            #print inst
            #x, y = inst.args
            #print 'x = ' , x
            #print 'y = ' , y
            #db.append(wikipedia.WikipediaPage(inst.options[1]))
            titles[i] = wikipedia.random(pages=1)
            page(titles)
    return db
        
pages = page(titles)

#print(pages[0])

contents = [i.content for i in pages]

#for i in contents:
#    print i
#    print "-----------------------------\n\n\n\n"
#print contents[0]
#clear_content = [i.capitalize for i in contents]
#print clear_content[0]

bloblist = [tb(i) for i in contents]
#bloblist=[]

score = []
"""
mod = md.Model()

#rf = tf(contents, [])


"""for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    l = []
    keys = scores.keys()
    for i in keys:
        if scores[i] < 0.0011 :
            l.append(i)
    for i in l:
        del scores[i]
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    score.append(scores)
adv = ad.Advise(None,mod)
res = adv.recommandation(score[0],score)
#for i in titles:
#    print i

for (i,j) in res:
    print j
"""


#    for word, score in sorted_words:
#        print("\tWord: {}, TF-IDF: {}".format(word.encode(errors='ignore'), format(score, '.5f')))
    
def generate (n):
    if n>0:
        title = wikipedia.random(pages=1)
        try:
            page = wikipedia.WikipediaPage(title)
            summary = page.summary
            content = tb(page.content)
            tff = {word: tf.tf(word,content) for word in content.words}
            res = {}
            for i in tff:
                if tff[i] == 0.0:
                    continue
                else:
                    res[i] = tff[i]
            article = art.Article(title, summary, kw=res, tfidf={})
            mod.insert(article)
            generate(n-1)
        except wikipedia.exceptions.DisambiguationError : 
            generate(n)
        except bson.errors.InvalidDocument :
            generate(n)

#generate(500)

#def test(n):
#    return mod.articles.find().limit(10)
"""
def propose(n):
    

propose(10)
"""
#res = test(10)
#for i in res:
#    print res["title"]

adv = ad.Advise(None,mod)

"""
def main():
    l = []
    l1 = []

    '''    articles = mod.articles.find()
    
    titles = []
    #articles = mod.articles.find()
    for i,v in enumerate(articles):
        titles.append((i, v["title"]))
    for (i,j) in titles:
        print("{}: {}".format( i,j.encode(errors='replace')))
    num = input('Enter a number\n')
    '''
    article = mod.articles.find().skip(int((time.time() % mod.articles.count()))).next()
    print article['title']

    articles = mod.articles.find()
    x = (article["title"], article["keywords"])

    for i in articles:
        l.append((i["title"], i["keywords"]))
    
    x1 = (x[0],{word: tf.tfidf(word, x[1], l) for word in x[1].keys()})
    for i in l:
        l1.append((i[0],{word: tf.tfidf(word, i[1], l) for word in i[1].keys()}))
    res =  adv.recommandation(x1,l1)    
    print("Recommandations pour {}:\n".format(article['title'].encode(errors='replace')))
    for (i,j) in res:
        if j > 0.5:
            print("{}: {}".format( i.encode(errors='replace') ,j))
        
"""

import time


class MyTimer:
    def __init__(self, tempo, target, args= [], kwargs={}):
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._tempo = tempo

    def _run(self):
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()
        self._target(*self._args, **self._kwargs)
        
    def start(self):
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()

    def stop(self):
        self._timer.cancel()


def set_tfidf():
    articles = mod.articles.find()
    res = []
    l = []
    for i in articles:
        l.append((i["title"],i["keywords"]))
    articles = mod.articles.find()
    for article in articles:
        #print article["title"]
        x = (article["title"],article["keywords"])
        tf_idf = {word: tf.tfidf(word, x[1], l) for word in x[1].keys()}
        mod.articles.update({"title":x[0]},{"$set" : {"tfidf":tf_idf}})        

def recommand(article, l):
    tfidf = []
    res = []
    for i in l:
        tfidf.append((i["title"],i["tfidf"]))
    rec = adv.recommandation(article["tfidf"],tfidf)
    for i in rec :
        if i in res:
            continue
        else :
            res.append(i)
    return res
            

def main():
    while 1:
        query = mod.articles.find({"like":True})
        articles = mod.articles.find({"like":False})
        try:
            for i in query:
                print "Start recommandation for article "
                print i["title"]
                thread.start_new_thread(recommand, (i, articles))
        except:
            print "Error: unable to start thread"
"""
    l = []
    l1 = []
    query = mod.articles.find({"like":True})
    articles = mod.articles.find()
    
    for i in articles:
        l.append((i["tfidf"])
        
    try:
        for i in query:
            threading.Thread(None, recommand, None, (i,l)).start()
            print "Start recommandation for article "
            print i["title"]
            #thread.start_new_thread(recommand, (i,l))
    except:
        print "Error: unable to start thread"


#    th = threading.Thread(None, recommand, None, (query,l))
#   while true:
#  th.start()
    while 1:
        pass
   """     


main()

