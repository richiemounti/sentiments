def compute_tweets():
    try:
        keywords = input('Enter keywords filename: ')
        read = open(keywords, 'r', encoding='utf-8')

        unhappy =  []
        satisfied = []
        happy = []

        for keyword in read:
            keyword = keyword.rstrip('\n')
            splitkeyword = keyword.split(',')
            if splitkeyword[1] == '1':
                unhappy.append(splitkeyword[0])
            elif splitkeyword[1] == '5':
                satisfied.append(splitkeyword[0])
            else:
                happy.append(splitkeyword[0])
        read.close()
    except IOError:
        print('Error: File', keywords, "does not exist")
        quit()




    try:
        tweets = input('Enter the tweet filename: ')
        read2 = open(tweets, 'r', encoding='utf-8')
        EasternTweets = 0
        PacificTweets = 0
        MountainTweets = 0
        CentralTweets = 0

        easternScore = 0
        pacificScore = 0
        mountainScore = 0
        centralScore = 0

        for tweet in read2:
            tweet = tweet.rstrip('\n')
            splittweet = tweet.split()

            latStrip1 = splittweet[0].rstrip(',')
            latStrip2 = latStrip1.lstrip('[')
            latitude = float(latStrip2)

            longStrip = splittweet[1].rstrip(']')
            longitude = float(longStrip)

            if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude <= -67.4446574 and longitude >= -87.518395) :
                originalEasternScore = 0
                for e in splittweet:
                    if e in unhappy:
                        easternScore += 1
                    elif e in satisfied:
                        easternScore += 5
                    elif e in happy:
                        easternScore += 10
                if originalEasternScore != easternScore:
                    EasternTweets += 1
                    originalEasternScore = easternScore

            if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude <= -87.518395 and longitude >= -101.998892) :
                originalCentralScore = 0
                for e in splittweet:
                    if e in unhappy:
                        CentralTweets += 1
                        centralScore += 1
                    elif e in satisfied:
                        CentralTweets += 1
                        centralScore += 5
                    elif e in happy:
                        CentralTweets += 1
                        centralScore += 10
                if originalCentralScore != centralScore:
                    CentralTweets += 1
                    originalCentralScore = centralScore

            if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude <= -101.998892 and longitude >= -115.236428) :
                originalMountainScore = 0
                for e in splittweet:
                    if e in unhappy:
                        MountainTweets += 1
                        mountainScore += 1
                    elif e in satisfied:
                        MountainTweets += 1
                        mountainScore += 5
                    elif e in happy:
                        MountainTweets += 1
                        mountainScore += 10
                if originalMountainScore != mountainScore:
                    MountainTweets += 1
                    originalMountainScore = mountainScore

            if (latitude <= 49.189787 and latitude >= 24.660845) and (longitude <= -115.236428 and longitude >= -125.242264) :
                originalPacificScore = 0
                for e in splittweet:
                    if e in unhappy:
                        PacificTweets +=1
                        pacificScore += 1
                    elif e in satisfied:
                        PacificTweets +=1
                        pacificScore += 5
                    elif e in happy:
                        PacificTweets +=1
                        pacificScore += 10
                if originalPacificScore != pacificScore:
                    PacificTweets +=1
                    originalPacificScore = pacificScore
        
        finalEasternScore =  easternScore / EasternTweets
        finalCentralScore =  centralScore / CentralTweets
        finalMountainScore = mountainScore / MountainTweets
        finalPacificScore =  pacificScore / PacificTweets

        print('Eastern zone has a score of', finalEasternScore, 'with', EasternTweets, 'tweets')
        print('Central zone has a score of', finalCentralScore, 'with', CentralTweets, 'tweets')
        print('Mountain zone has a score of', finalMountainScore, 'with', MountainTweets, 'tweets')
        print('Pacific zone has a score of', finalPacificScore, 'with', PacificTweets, 'tweets')

        read2.close()

    except IOError:
        print('Error: File', tweets, 'does not exist.')
        quit()
    