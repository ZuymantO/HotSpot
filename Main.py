#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import pymongo
import string
import math
#import tfidf
import wikipedia
from textblob import TextBlob as tb
import Model as md
import TfIdf as tf
import Advise as ad
import Article as art
import bson

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
            article = art.Article(title, summary, kw=res)
            mod.insert(article)
            generate(n-1)
        except wikipedia.exceptions.DisambiguationError : 
            generate(n)
        except bson.errors.InvalidDocument :
            generate(n)

#generate(10)

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


def testidf():
    l = []
    l1 = []
    article = mod.getOneArticle()
    articles = mod.articles.find()
    x= (article["title"],article["keywords"])
    for i in articles:
        l.append((i["title"],i["keywords"]))
    x1 = (x[0],{word: tf.tfidf(word, x[1], l) for word in x[1].keys()})
    for i in l:
        l1.append((i[0],{word: tf.tfidf(word, i[1], l) for word in i[1].keys()}))
    res = adv.recommandation(x1,l1)    
    for (i,j) in res:
        print("{}: {}".format( i.encode(errors='ignore') ,j))
testidf()
    

    
