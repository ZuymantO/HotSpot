#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import pymongo
import string
import math
#import tfidf
import wikipedia
from textblob import TextBlob as tb
import Model as md
#from TfIdf import TfIdf as tf

stop_words=["le","la","les","un","une","de","des","en","du","l'","mais","ou","et","donc","or","ni","car","ces","ce","sa","mon","ton","son","leur","leurs","je","tu","il","elle","on","nous","vous","ils","elles"
            ,"mes","tes","nos","vos",
            "Le","La","Les","Un","Une","De","Des","En","Du","L'","Mais","Ou","Et","Donc","Or","Ni","Car","Ces","Ce","Sa","Mon","Ton","Son","Leur","Leurs","Je","Tu","Il","Elle","On","Nous","Vous","Ils","Elles"
            ,"Mes","Tes","Nos","Vos"]

def tf(word, blob):
    x = blob.words.count(word)
    y = len(blob.words)
    #print x
    #print y
    return x/(y*1.0)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    if word in stop_words:
        return 0.0
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

wikipedia.set_lang("fr")
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


def scalaire(x,y):
    sum = 0.0
    for i in x:
        sum = sum + x[i]*y[i]
    return sum


def cosinus(x,y):
    for i in x.keys():
        if i in y:
            continue
        else:
            y[i]=0.0
    for i in y.keys():
        if i in x:
            continue
        else:
            x[i]=0.0
    scal = scalaire(x,y)
    scalx = scalaire(x,x)
    scaly = scalaire(y,y)
    res = scal/(scalx*scaly)
    return res
    
def recommandation(x,l):
    res = []
    for i in range(len(l)):
        if cosinus(x,l[i])<0.9:
            continue
        else:
            res.append(i)
    return res

score = []

#mod = md.Model()

#rf = tf(contents, [])


for i, blob in enumerate(bloblist):
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
    #score.append(scores)


#res = recommandation(score[0],score)
#for i in titles:
#    print i

#for i in res:
#    print i



    for word, score in sorted_words:
        print("\tWord: {}, TF-IDF: {}".format(word.encode(errors='ignore'), format(score, '.5f')))
    

