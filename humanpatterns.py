### Human identifiable patterns for Sarcasm detection
## @author: Aparna N
## @author: Apoorva Rao B
## @author: Karthik

import math
import re
import collections as coll
import numpy


#pattern set-Individual words - 3
# really,realy realllly
# sure,shurre, surre, surely etc
# Wooowww, wow etc
# Ohh, oh, O
# yeah, yeaah
# thanks
# great, grrreat
# crraaaaazzzyyy
# seriously
# haha, ahahaha
# stupid
# Noooo
# sheeesh
# soooo, 
# Btw, btw that's
# whaaaaaat
# Neverrrrr
# lolololol

def individualwords(tweet):
	patternReList=[r"(\s|^)reall+y(\s|$|!|\.|\?)",r"(\s|^)sh?urr+e(\s|$|!|\.|\?)",r"(\s|^)wo+w(\s|$|!|\.|\?)",r"(\s|^)oo+h*|ohh+(\s|$|!|\.|\?)",r"(\s|^)yeaa+h(\s|$|!|\.|\?)",r"(\s|^)thanks(\s|$|!|\.|\?)",r"(\s|^)stupid(\s|$|!|\.|\?)",r"(\s|^)noo+(\s|$|!|\.|\?)",r"(\s|^)shee+sh(\s|$|!|\.|\?)",r"(\s|^)g(rr+eat)(\s|$|!|\.|\?)|(\s|^)grr+8(\s|$|!|\.|\?)",r"(\s|^)cr+a+z+y+(\s|$|!|\.|\?)",r"(\s|^)seriously(\s|$|!|\.|\?)",r"(\s|^)ha(ha)+|ah(ah)+(\s|$|!|\.|\?)",r"(\s|^)soo+(\s|$|!|\.|\?)",r"(\s|^)btw(\sthat's)?(\s|$|!|\.|\?)",r"(\s|^)whaa+t(\s|$|!|\.|\?)",r"(\s|^)neverr+(\s|$|!|\.|\?)",r"(\s|^)(lol)+(\s|$|!|\.|\?)"]
	
	contr = 0
	res = []
	for word in patternReList:
		res += re.findall(word, tweet,re.IGNORECASE)
	if(len(res)>0):
		#print 1
		contr = math.tanh(float(len(res))/2)
	return contr
		

#pattern set-Unnecessary Capitalization - 1
# LOVE, LOOOVE
# ZERO
# THAT
# AWESOME
# EVER
# REAL
# HUGE
# ADORE
# ACTUALLY
# ALL
# NOT
# WHAT A SURPRISE
# GREAT 

def unnecessaryCapitalization(tweet):
	
	patternReList=[r"(\s|^)LO+VE(\s|$|/.|!|/?)",r"(\s|^)ZERO(\s|$|/.|!|/?)",r"(\s|^)THAT(\s|$|/.|!|/?)",r"(\s|^)AWESOME(\s|$|/.|!|/?)",r"(\s|^)EVER(\s|$|/.|!|/?)",r"(\s|^)REAL(\s|$|/.|!|/?)",r"(\s|^)HUGE(\s|$|/.|!|/?)",r"(\s|^)ADORE(\s|$|/.|!|/?)",r"(\s|^)ACTUALLY(\s|$|/.|!|/?)",r"(\s|^)ALL(\s|$|/.|!|/?)",r"(\s|^)NOT(\s|$|/.|!|/?)",r"(\s|^)WHAT A SURPRISE(\s|$|/.|!|/?)",r"(\s|^)GREAT(\s|$|/.|!|/?)"]
	
	contr = 0
	res = []
	for word in patternReList:
		res+=re.findall(word, tweet)
	if(len(res)>0):
		#print 2
		contr = math.tanh(float(len(res))/2)
	return contr
		
	
	
	

#pattern set- Punctuations - 2
# multiple !
# multiple ?
# intermixed !?!??
# ellipsis more than once ... (repetition)
# longer than 3 dots ..... or with spaces . . .

def punctuations(tweet):
	
	patternReList=[r"\S[!\?][!(\?)]+",r"\.\s?\.\s?(\.\s?)+"]
	
	contr = 0
	res = []
	for word in patternReList:
		res+=re.findall(word, tweet,re.IGNORECASE)
	if(len(res)>0):
		#print 3
		contr = math.tanh(float(len(res))/2)
	return contr
			 

#pattern set- emoticons - 2
# ;)
# :P
# ^___^
# (':
# (;

def emoticons(tweet):
	
	patternReList=[r"[;]['\-,]?\)",r"\(['\-,]?[;:]",r"\^_+\^",r"[;|:]['\-,]?p"]
	
	contr = 0
	res = []
	for word in patternReList:
		res+=re.findall(word, tweet,re.IGNORECASE)
	if(len(res)>0):
		#print 4
		contr = math.tanh(float(len(res))/2)
	return contr
		
	
	

#pattern set- words repeated multiple times - 3
#really really
# so so so

def repeatedWords(tweet):
	
	patternReList=[r"(\s|^)really (really)+(\s|$|/.|!|/?)",r"(\s|^)so (so)+(\s|$|/.|!|/?)"]
	
	contr = 0
	res = []
	for word in patternReList:
		res+=re.findall(word, tweet,re.IGNORECASE)
	if(len(res)>0):
		#print 5
		contr = math.tanh(float(len(res))/2)
	return contr
			
		
	

#pattern set- combination of words - 3
# just fantastic
# Oh joy
# Ohh yeah
# Real shocker
# so original
# care so much

def combinationOfWords(tweet):
	
	patternReList=[r"(\s|^)just fantastic(\s|$|/.|!|/?)",r"(\s|^)Oh joy(\s|$|/.|!|/?)",r"(\s|^)Oh+ yeah(\s|$|/.|!|/?)",r"(\s|^)real shocker(\s|$|/.|!|/?)",r"(\s|^)so (fucking)? original(\s|$|/.|!|/?)",r"(\s|^)care so much(\s|$|/.|!|/?)"]
	
	contr = 0
	res = []
	for word in patternReList:
		res+=re.findall(word, tweet,re.IGNORECASE)
	if(len(res)>0):
		#print 6
		contr = math.tanh(float(len(res))/2)
	return contr
	
	
			 
# pattern set-Cuss words- what if there are stars in between like f**k? - 2
# fucking, fuckin, fuck
# bitch
# stfu
# gfu
# suckkk
# sick
# shit
# motherfucker
# cocksucker
# tits
# wtf
# piss
# slut
# asshole

def badWords(tweet):
	
	
	badWordsList=["fucking", "fuckin","ff+uu+c*k*","f\*+k","[a-b]+[\*#\$\%]+[a-b]+", "fuck","bitch","stfu","gfu","suck","sick","shit","motherfucker","cocksucker","tits","wtf","piss","slut","asshole"]
	
	contr = 0
	res = []
	for badWord in badWordsList:
		res+=re.findall(r"(\s|^)%s(\s|$|/.|!|/?)"%badWord, tweet,re.IGNORECASE)
	if(len(res)>0):
		#print 7
		contr = math.tanh(float(len(res))/2)
	return contr
				


#pattern set- specific hashtags - 3
#sarcasm - WE SHOULD NOT CONSIDER THIS HASH TAG...
#whyme
#foryoudumbfolk
#booyah
#PleaseJustKeepTrying
#ihatethis
#burns
#lmao
#thanksfortheadvice
#notreally
#feelingthelove
#shutup
#comeon
#thoughtwewerefriends
#getmeoutofhere
#shootmenow
#disgust
#idontreallycare
#retarded
#bazinga
#soexcited
#killmenow

def specificHashtags (tweet):
	
	specificHashtagsList=["#killmenow","#whyme","#foryoudumbfolk","#booyah","#PleaseJustKeepTrying","#ihatethis","#burns","#lmao","#thanksfortheadvice","#notreally","#feelingthelove","#shutup","#comeon","#thoughtwewerefriends","#getmeoutofhere","#shootmenow","#disgust","#idontreallycare","#retarded","#bazinga","#soexcited"]
	
	contr = 0
	res = []
	for specificHashtag in specificHashtagsList:
		res+=re.findall(r"%s(\s|$)"%specificHashtag, tweet,re.IGNORECASE)
	if(len(res)>0):
		#print 8
		contr = math.tanh(float(len(res))/2)
	return contr

#patternset- capitalization of the entire tweet - 3
# eg "WUT'S THE SCORE AT THE HALF ......#SARCASM LOL"

def totallyUpperCase (tweet):
	
	contr = 0
	res = []
	res+=re.findall(r"^[^a-z]+$", tweet)
	if(len(res)>0):
		#print 9
		contr = math.tanh(float(len(res))/2)
	return contr




def testPatterns(tweet):
	patternWeightArray = [
		individualwords(tweet),
		unnecessaryCapitalization(tweet),
		punctuations(tweet),
		emoticons(tweet),
		repeatedWords(tweet),
		combinationOfWords(tweet),
		badWords(tweet),
		specificHashtags(tweet),
		totallyUpperCase (tweet)
	]

	return patternWeightArray
	
	

def getRating(tweet):
	weights = [3,1,2,2,3,3,2,3,3]
	patternWeightArray = testPatterns(tweet)

	w = numpy.array(weights)
	pw = numpy.array(patternWeightArray)

	#print weights
	#print patternWeightArray
	#print w.shape
	#print pw.shape
	
	## tanh()	
	#print 3 * math.tanh(sum(map(lambda x,y: x * y, weights, patternWeightArray)))/(sum(contrWeights)+0.1)	
	
	## x/(1 + x*x)
	#print 3 * math.sqrt(sum(map(lambda x,y: x * y, weights, patternWeightArray)))
	
	## 1/(1+|x|)
	#x = 1.0 * sum(map(lambda x,y: x * y, weights, patternWeightArray))
	x = 1.0 * sum(w*pw)
	rating = 2*((1.0 * x)/(1 + x)) + 1

	return rating
		


# Correlation between patterns? 
# sarcastic tweets commonly have indications of tweeters being ignored by friends or a loved one. May also be sleep deprived or just generally grumpy. 

# TEST DRIVER FOR TESTING THE MODULE INDEPENDENTLY
if __name__ == '__main__':
	
	#tweet=":-p"
	#tweet="You are sooo damn smart. Fuck you bitch. You're so fucking original"
	#tweet="f**k! #killmenow really really! Oh Joy...thanks stupid EVER ADORE sheeesh noooo????? :-p"
	#tweet="F**K! #KILLMENOW REALLY REALLY! OH JOY...THANKS STUPID EVER ADORE SHEESH NOOOO????? :-P F**K! #KILLMENOW REALLY REALLY! OH JOY...THANKS STUPID EVER ADORE SHEESH NOOOO????? :-P F**K! #KILLMENOW REALLY REALLY! OH JOY...THANKS STUPID EVER ADORE SHEESH NOOOO????? :-P  F**K! #KILLMENOW REALLY REALLY! OH JOY...THANKS STUPID EVER ADORE SHEESH NOOOO????? :-P  F**K! #KILLMENOW REALLY REALLY! OH JOY...THANKS STUPID EVER ADORE SHEESH NOOOO????? :-P F**K! #KILLMENOW REALLY REALLY! OH JOY...THANKS STUPID EVER ADORE SHEESH NOOOO????? :-P F**K! #KILLMENOW REALLY REALLY! OH JOY...THANKS STUPID EVER ADORE SHEESH NOOOO????? :-P F**K! #KILLMENOW REALLY REALLY! OH JOY...THANKS STUPID EVER ADORE SHEESH NOOOO????? :-P F**K! #KILLMENOW REALLY REALLY! OH JOY...THANKS STUPID EVER ADORE SHEESH NOOOO????? :-P F**K! #KILLMENOW REALLY REALLY! OH JOY...THANKS STUPID EVER ADORE SHEESH NOOOO????? :-P F**K! #KILLMENOW REALLY REALLY! OH JOY...THANKS STUPID EVER ADORE SHEESH NOOOO????? :-P F**K! #KILLMENOW REALLY REALLY! OH JOY...THANKS STUPID EVER ADORE SHEESH NOOOO????? :-P"
	#tweet="really really soooo good :P "
	#tweet="Your comments are sooo witty! #killmenow"
	tweet="your work is soo original! WOW :-P"
	#tweet="this is just GREAT!"
	#tweet="I WISH I WERE YOU!"
	#tweet="I LOVE POTATO KRISPER AT KFC.  THEY ARE GREAT!?!?"
	#tweet="I love KFC"
	#tweet="Visiting Bangalore for a talk today."
	#tweet = "RT REF BREAKING NEWS: Chickens killed in crash LINK sure whether to laugh or not. ..  ???"
	#tweet = "REF lol...thanks but no thanks, I dont use the twitter page enough to PAY for something!"
	#tweet = "HEY"
	#tweet = "back to net beans?....going BACK to trees??????"
	

	rating = getRating(tweet)
	print rating
	
	


