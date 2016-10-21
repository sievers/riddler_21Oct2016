f=open('twl.txt')      #for US scrabble
#f=open('sowpods.txt') #for UK scrabble
words=f.readlines();
f.close()

words.sort(key=len) #make sure words are sorted by length
mydict={}
for word in words:
    word=word.strip() #ditch annoying newline
    if (len(word)==2):  #all 2-letter words are valid
        mydict[word]=True
    else:
        if mydict.has_key(word[1:]): #if end of word is another word, enter into dictionary.
            mydict[word]=word[1:]    #make dictionary entry the shorter word for convenience
        if mydict.has_key(word[0:-1]):  #now check first part of word
            mydict[word]=word[0:-1]
keys=mydict.keys()  #valid words are now the python dictionary keys
keys.sort(key=len)  #sort 'em by length and then print the last key
print 'longest key has length ', len(keys[-1])

