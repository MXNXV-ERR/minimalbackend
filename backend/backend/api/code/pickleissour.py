import joblib
import pandas as pd
from textblob import TextBlob
import nltk

nltk.download('punkt')
import re
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize

array_Noun = []
array_Adj = []
array_Verb = []
array_Adv = []
array_Pro = []
array_Pre = []
array_Con = []
array_Art = []
array_Nega = []
array_Aux = []

articles = ['a', 'an', 'the']
negations = ['no', 'not', 'none', 'nobody', 'nothing', 'neither', 'nowhere', 'never', 'hardly', 'barely', 'scarcely']
auxilliary = ['am', 'is', 'are', 'was', 'were', 'be', 'being', 'been', 'will', 'would', 'shall', 'should', 'may', 'might', 'must', 'can', 'could', 'do', 'does', 'did', 'have', 'having', 'has', 'had']


def getJoblibModelPred(review):
    print(review)
    model=joblib.load(open('api/code/olt_finalllllllll.pkl','rb'))
    
    # pred =model.predict([["10.4","15.2","12","132","0","123","21","2","1","2","3"]])
    # print(pred[0])
    # class_names = ['Fake', 'Genuine']
    # return class_names[pred[0]] 



    rev = review['text']
    rat = review['rating']
    use = review['useful']
    #print(reviews)
    # sentiment_score = []
    # sentiment_subjectivity=[]
    # review_head_sentiment=[]
    testimonial = TextBlob(rev)
    sentiment_score=testimonial.sentiment.polarity
    sentiment_subjectivity=testimonial.sentiment.subjectivity
    text = rev 
    filter = re.sub('[^\w\s]', '', text)
    conver_lower = filter.lower()
    Tinput = conver_lower.split(" ")
    
    for i in range(0, len(Tinput)):
        Tinput[i] = "".join(Tinput[i])
    UniqW = Counter(Tinput)
    s = " ".join(UniqW.keys())
    
    tokenized = sent_tokenize(s)
    
    for i in tokenized:
        wordsList = nltk.word_tokenize(i)
        #wordsList = [w for w in wordsList if not w in stop_words]
        
        Art = 0
        Nega = 0
        Aux = 0
        for word in wordsList:
            if word in articles:
                Art += 1
            elif word in negations:
                Nega += 1
            elif word in auxilliary:
                Aux += 1
                
        tagged = nltk.pos_tag(wordsList)
        counts = Counter(tag for word,tag in tagged)

        N = sum([counts[i] for i in counts.keys() if 'NN' in i])
        Adj = sum([counts[i] for i in counts.keys() if 'JJ' in i])
        Verb = sum([counts[i] for i in counts.keys() if 'VB' in i])
        Adv = sum([counts[i] for i in counts.keys() if 'RB' in i])
        Pro = sum([counts[i] for i in counts.keys() if (('PRP' in i) or ('PRP$' in i) or ('WP' in i) or ('WP$' in i))])
        Pre = sum([counts[i] for i in counts.keys() if 'IN' in i])
        Con = sum([counts[i] for i in counts.keys() if 'CC' in i])
        word_count = len(rev.split())
      
        uniqWords=len(set(rev.split()))

        words = rev.split()
        neg = 0
        for w in words:
            testimonial = TextBlob(w)
            score = testimonial.sentiment.polarity
            if score < 0:
                neg += 1
        auth = (Pro + uniqWords - neg)/word_count
        AT = 30+(Art+Pre-Pro-Aux-Adv-neg-Con)

        pred = model.predict([[rat,use,sentiment_score,sentiment_subjectivity,word_count,N,Adj,Verb,Adv,auth,AT]])
        class_names = ['Fake', 'Genuine']
        print(class_names[pred[0]])
        return class_names[pred[0]]




