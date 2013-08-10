### CLASSIFIYING THE GIVEN TWEET for Sarcasm detection
##  @author karthik
##    @date 18 Oct 2012
##    @date 23 Nov 2012

import classifier

from train.preProcessor import *
from train.patternExtractor import *
from train.featureVectorBuilder import *


#####################################################################################
#####################################################################################

def preProcess(tweet):
    tweetDict=coll.defaultdict(int)
    tweetDict[tweet] = "?"

    wordDict = buildWordDict(tweetDict.keys())

    processedTweetDict = generalizeWords(tweetDict)

    useableTweetDict = replaceContentWord(processedTweetDict, wordDict)

    return useableTweetDict

#####################################################################################
#####################################################################################

def getFeatureVector(useableTweetDict):
    #load pre-determined patterns
    s_patterns = open("./train/data/patterns", "r").read()

    #make it into an array
    patterns = eval(s_patterns)

    #build feature vector for the current tweet
    featureVectors = buildFeatureVectors(useableTweetDict, patterns)
    
    # return the feature vector of the first tweet
    return featureVectors.values()[0]

#####################################################################################
#####################################################################################

'''
def getRatingOrange(tweet):
    #pre process
    useableTweetDict = preProcess(tweet)

    #build feature vector
    fv = getFeatureVector(useableTweetDict)

    #load feature vectors of trained data
    trainSetFV = o.data.Table("./train/data/feature_vectors")

    #load the knn classifier
    knn = o.classification.knn.kNNLearner(trainSetFV, k=8)

    #prepare the feature vector for classification
    domain = trainSetFV.domain
    fv.append("?")
    inst = o.data.Instance(domain, fv)

    #classify the instance
    rating = knn(inst)

    return rating

'''

#####################################################################################
#####################################################################################



def loadTrainSetFV():
    f = open("./train/data/feature_vectors.tab", "r")

    trainSetFV = []
    trainLabels = []

    i = 0
    for line in f:
        #skip the first 3 lines...they are domain info
        if i < 4:
            i+=1
            continue

        vec = line.strip(" \n\t").split("\t")
        trainSetFV.append([float(ele) for ele in vec[2:]])    #features
        trainLabels.append(int(vec[1]))                     #sarcasm rating

    return trainSetFV, trainLabels



def getRating(tweet):
    #pre process
    useableTweetDict = preProcess(tweet)

    #build feature vector
    fv = getFeatureVector(useableTweetDict)

    #load feature vectors of trained data
    trainSetFV, trainLabels = loadTrainSetFV()   #array of arrays, array

    #load the knn classifier
    knn = classifier.KNN(k=8)

    #train the classifier
    knn.train(trainSetFV, trainLabels)

    #classify the instance
    rating = knn.predict(fv)

    return rating



if __name__ == "__main__":
    tweet = "You are sooo damn smart. Fuck you bitch. You're so fucking original"
    #tweet = "your work is soo original!"
    #tweet = "Your comments are sooo witty! #killmenow"
    #tweet = "I LOVE POTATO KRISPER AT KFC.  THEY ARE GREAT!?!?"
    tweet = "twice in one month.. come on now... seriously???"

    tweetFile = open("../trainingdata/tweets_sarcastic.txt", "r")
    
    n = 0
    s = 0
    for tweet in tweetFile:
        r = getRating(tweet)
        if r == 1:
            n+=1
        else:
            s+=1

    print s,n
