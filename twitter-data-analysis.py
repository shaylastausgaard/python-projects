'''
Shayla Stausgaard
OBJECTIVE: The objective is to determine which timezone (Eastern, Central, Mountain, Pacific; is the “happiest”.

'''
keywordDict = {} #create empty dictionary to handle exceptions if there is no keyword in the tweet being assessed
tweets = []
pacificScore = []
mountainScore = []
centralScore = []
easternScore = []
import happy_histogram
p1 = (49.189787, -67.444574)
p2 = (24.660845, -67.444574)
p3 = (49.189787, -87.518395)
p4 = (24.660845, -87.518395)
p5= (49.189787, -101.998892)
p6 = (24.660845, -101.998892)
p7 = (49.189787, -115.236428)
p8 = (24.660845, -115.236428)
p9 = (49.189787, -125.242264)
p10 = (24.660845, -125.242264)

#open keyword file and handle exceptions
keyWordsFile = input("Please enter the name of the file containing your keywords: ")
if not keyWordsFile.endswith('.txt'):
    keyWordsFile = keyWordsFile + '.txt'
try:
    infile = open(keyWordsFile, "r", encoding="utf-8")
    for line in infile:
        line = line.split(',')
        keywordDict[line[0]] = int(line[1].strip())
    infile.close()
except IOError:
    print("Error: File not found, please enter a valid file name. ")


#open tweet file and handle exceptions
tweetFile = input("Please enter the name of the file with your downloaded Tweets: ")
if not tweetFile.endswith('.txt'):
    keyWordsFile = tweetFile + '.txt'
try:
    fileWithTweets = open(tweetFile, "r", encoding="utf-8")
    for line in fileWithTweets:
        data = line.split()
        tweetParts = [data[0].strip("[,"), data[1].strip("]"), data[5:(len(data)-1)]]
        tweets.append(tweetParts)
    fileWithTweets.close()
except IOError:
    print("Error: File not found, please enter a valid file name. ")

#function to generate sentiment value (happiness score)
def sentimentValue(regionList, tweet):
    found = False
    tweetScore = 0
    count = 0
    for word in tweet:
        if word in keywordDict:
            tweetScore = tweetScore + keywordDict[word]
            count = count + 1

    if tweetScore > 0:
        regionList.append(tweetScore/count)
currentNum = 0
while currentNum < len(tweets):
    latitude = tweets[currentNum][0]
    longitude = tweets[currentNum][1]
    currentTweet = tweets[currentNum][2]

    if float(p2[0]) <= float(latitude) <= float(p1[0]) and float(p9[1]) <= float(longitude) <= float(p7[1]):
        sentimentValue(pacificScore, currentTweet)
    elif float(p2[0]) <= float(latitude) <= float(p1[0]) and float(p7[1]) <= float(longitude) <= float(p5[1]):
        sentimentValue(mountainScore, currentTweet)
    elif float(p2[0]) <= float(latitude) <= float(p1[0]) and float(p5[1]) <= float(longitude) <= float(p3[1]):
        sentimentValue(centralScore, currentTweet)
    elif float(p2[0]) <= float(latitude) <= (p1[0]) and float(p3[1]) <= float(longitude) <= float(p1[1]):
        sentimentValue(easternScore, currentTweet)
    currentNum = currentNum + 1

# #final happiness score calculation
pScore = sum(pacificScore) / len(pacificScore)
mScore = sum(mountainScore)/ len(mountainScore)
cScore = sum(centralScore) / len(centralScore)
eScore = sum(easternScore) / len(easternScore)
pScore = round(pScore,1)
mScore = round(mScore,1)
cScore = round(cScore,1)
eScore = round(eScore,1)

#print statements(happiness score for each timezone and number of tweets.txt in that time zone)
print(' ')
print('The happiness score for Pacific time zone: ',pScore)
print('Total number of Tweets in Pacific time zone: ', len(pacificScore))
print('')
print('The happiness score for Mountain time zone: ', mScore)
print('The total number of Tweets in Mountain time zone: ', len(mountainScore))
print(' ')
print('The happiness score for Central time zone: ',cScore)
print('Total number of Tweets in Central time zone: ', len(centralScore))
print(' ')
print('The happiness score for Eastern time zone: ', eScore,)
print('Total number of Tweets in Eastern time zone: ', len(easternScore))

happy_histogram.drawSimpleHistogram(pScore, mScore, cScore, eScore)



