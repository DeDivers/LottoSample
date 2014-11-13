import random

def todayCouldBeTheDay(number):
    playerNumbers = []
    lottoNumbers = []
    powerBall = []
    playerPowerBall = []
    numbers = 0
    numCorrect = 0
    pick6 = 0
    power = 0



    if number <=30 and number >4:


        if number == 6:
            while pick6 < 5:

                x = random.random() * 59 +1
                px = input("Pick a number between 1 and 59")
                x = int(x)
                px = int(px)
                if x in lottoNumbers:
                    pick6 = pick6
                    print("Please reinput number")
                elif px in playerNumbers:
                    pick6 = pick6
                    print("Number already chosen. Pick another.")
                else:

                    lottoNumbers.append(x)
                    playerNumbers.append(px)
                    pick6 += 1
            if pick6 == 5:

                pb = random.random() * 35 +1
                ppb = input("Pick a number between 1 and 35")
                pb = int(pb)
                ppb = int (ppb)
                powerBall.append(pb)
                playerPowerBall.append(ppb)
                pick6 += 1

            for n in range (0,5):
                if playerNumbers[n] in lottoNumbers:

                    numCorrect += 1
            if playerPowerBall == powerBall:
                power += 1
            listPow = [numCorrect, power]
            return listPow


        for lotto in range (0, number):
            x = random.random() * 70
            x = int(x)
            if x in lottoNumbers:
                x = random.random() * 70
                x = int(x)
                if x in lottoNumbers:
                    x = random.random() * 70
                    x = int(x)
                    if x in lottoNumbers:
                        x = random.random() * 70
                        x = int(x)
                    else:
                        lottoNumbers.append(x)
                else:
                    lottoNumbers.append(x)
            else:
                lottoNumbers.append(x)
        while numbers < number:
            inp = input("Pick a number between 0 and 69")
            inpt = int(inp)
            if inpt < 70:
                if inpt in playerNumbers:
                    print("Number already in list. Try again!")
                    numbers = numbers
                else:
                    playerNumbers.append(inpt)
                    numbers += 1
            else:
                print("Incorrect input. Try again!")
                numbers = numbers


    elif number == 4:
        for lotto in range (0, number):
                x = random.random() * 25 +1
                x = int(x)
                if x in lottoNumbers:
                    x = random.random() * 25 +1
                    x = int(x)
                    if x in lottoNumbers:
                        x = random.random() * 25 + 1
                        x = int(x)
                        if x in lottoNumbers:
                            x = random.random() * 25 + 1
                            x = int(x)
                        else:
                            lottoNumbers.append(x)
                    else:
                        lottoNumbers.append(x)
                else:
                    lottoNumbers.append(x)
        while numbers < number:
            inp = input("Pick a number between 1 and 25")
            inpt = int(inp)
            if inpt <= 25:
                if inpt in playerNumbers:
                    print("Number already in list. Try again!")
                    numbers = numbers
                else:
                    playerNumbers.append(inpt)
                    numbers += 1
            else:
                print("Incorrect input. Try again!")
                numbers = numbers


    elif number == 3:
        for lotto in range (0, number):
            x = random.random() * 9 + 1
            x = int(x)
            if x in lottoNumbers:
                x = random.random() * 9 + 1
                x = int(x)
                if x in lottoNumbers:
                    x = random.random() * 9 + 1
                    x = int(x)
                    if x in lottoNumbers:
                        x = random.random() * 9 + 1
                        x = int(x)
                    else:
                        lottoNumbers.append(x)
                else:
                    lottoNumbers.append(x)
            else:
                lottoNumbers.append(x)
        while numbers < number:
            inp = input("Pick a number between 1 and 9. \n(Note: Numbers have to match the exact \norder for them to be counted as correct.)")
            inpt = int(inp)
            if inpt < 10:
                playerNumbers.append(inpt)
                numbers += 1
            else:
                print("Incorrect input. Try again!")
                numbers = numbers
        for n in range (0, 3):
            if playerNumbers[n] == lottoNumbers[n]:
                numCorrect += 1
            else:
                numCorrect = numCorrect
        if numCorrect == numbers:
            print (lottoNumbers)
            print (playerNumbers)
            print("You win the Jackpot! All numbers matched!")
            return("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        else:
            print (lottoNumbers)
            print (playerNumbers)
            print("You got", numCorrect, "/", numbers, "correct. Better luck next time!")
            return("Y U so poor")


    elif number == 2 or number == 1 or number == 0:
        print("Invalid number of numbers to pick for lottery. Defaulting to 3 numbers.")
        return todayCouldBeTheDay(3)


    elif number > 30 and number <= 100:
        for lotto in range (0, number):
            x = random.random() * 1000
            x = int(x)
            if x in lottoNumbers:
                x = random.random() * 1000
                x = int(x)
                if x in lottoNumbers:
                    x = random.random() * 1000
                    x = int(x)
                    if x in lottoNumbers:
                        x = random.random() * 1000
                        x = int(x)
                    else:
                        lottoNumbers.append(x)
                else:
                    lottoNumbers.append(x)
            else:
                lottoNumbers.append(x)
        while numbers < number:
            inp = input("Pick a number between 0 and 999")
            inpt = int(inp)
            if inpt < 1000:
                if inpt in playerNumbers:
                    print("Number already in list. Try again!")
                    numbers = numbers
                else:
                    playerNumbers.append(inpt)
                    numbers += 1
            else:
                print("Incorrect input. Try again!")
                numbers = numbers

    else:
        print("Odds too low for the player. Defaulting to 10 numbers.")
        return todayCouldBeTheDay(10)


    for n in range (0, len(playerNumbers)):
        if playerNumbers[n] in lottoNumbers:
            numCorrect += 1
        else:
            numCorrect = numCorrect
    if numCorrect == numbers:
        print (lottoNumbers)
        print (playerNumbers)
        print("You win the Jackpot! All numbers matched!")
        return("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    else:
        print (lottoNumbers)
        print (playerNumbers)
        print("You got", numCorrect, "/", numbers, "correct. Better luck next time!")
        return("Y U so poor")





def lotRand(number):
    playerNumbers = []
    lottoNumbers = []
    powerBall = []
    playerPowerBall = []
    numbers = 0
    pick6 = 0
    numCorrect = 0
    lotto = 0
    power = 0


    if number <=30 and number >4:
        if number == 6:
            while pick6 < 5:

                x = random.random() * 59 +1
                px = random.random() * 59 +1
                x = int(x)
                px = int(px)
                if x in lottoNumbers:
                    pick6 = pick6
                elif px in playerNumbers:
                    pick6 = pick6
                else:

                    lottoNumbers.append(x)
                    playerNumbers.append(px)
                    pick6 += 1
            if pick6 == 5:

                pb = random.random() * 35 +1
                ppb = random.random() * 35 +1
                pb = int(pb)
                ppb = int (ppb)
                powerBall.append(pb)
                playerPowerBall.append(ppb)
                pick6 += 1

            for n in range (0,5):
                if playerNumbers[n] in lottoNumbers:

                    numCorrect += 1
            if playerPowerBall == powerBall:
                power += 1
            listPow = [numCorrect, power]
           
            return listPow


        while lotto < number:

            x = random.random() * 60
            x = int(x)
            if x in lottoNumbers:
                lotto = lotto
            else:
                lottoNumbers.append(x)
                lotto += 1
        while numbers < number:
            x2 = random.random() * 60
            x2 = int(x2)
            if x2 < 70:
                if x2 in playerNumbers:

                    numbers = numbers
                else:
                    playerNumbers.append(x2)
                    numbers += 1
            else:
                print("Incorrect input. Try again!")
                numbers = numbers


    elif number == 4:
        while lotto < number:

            x = random.random() * 25 +1
            x = int(x)
            print(x)
            if x in lottoNumbers:

                lotto = lotto
            else:

                lottoNumbers.append(x)
                lotto += 1
        while numbers < number:

            x2 = random.random() * 25 +1
            x2 = int(x2)
            print(x2)
            if x2 in playerNumbers:


                numbers = numbers
            else:

                playerNumbers.append(x2)
                numbers += 1


    elif number == 3:
        while lotto < number:

            x = random.random() * 9 + 1
            x = int(x)
            lottoNumbers.append(x)
            lotto += 1

        while numbers < number:

            x2 = random.random() * 9 + 1
            x2 = int(x2)


            playerNumbers.append(x2)
            numbers += 1

        for n in range (0, 3):
            if playerNumbers[n] == lottoNumbers[n]:
                numCorrect += 1
            else:
                numCorrect = numCorrect
        if numCorrect == number:

            #print("You win the Jackpot! All numbers matched!")
            return(numCorrect)
        else:

            #print("You got", numCorrect, "/", numbers, "correct. Better luck next time!")
            return(numCorrect)


    elif number == 2 or number == 1 or number == 0:
        print("Invalid number of numbers to pick for lottery. Defaulting to 3 numbers.")
        return lotRand(3)


    elif number > 30 and number <= 100:
        while lotto < number:
            x = random.random() * 1000
            x = int(x)
            if x in lottoNumbers:
                lotto = lotto
            else:
                lottoNumbers.append(x)
                lotto += 1
        while numbers < number:
            x2 = random.random() * 1000
            x2 = int(x2)
            if x2 < 1000:
                if x2 in playerNumbers:

                    numbers = numbers
                else:
                    playerNumbers.append(x2)
                    numbers += 1
            else:
                print("Incorrect input. Try again!")
                numbers = numbers

    else:
        print("Odds too low for the player. Defaulting to 10 numbers.")
        return lotRand(10)


    for n in range (0, len(playerNumbers)):
        if playerNumbers[n] in lottoNumbers:
            numCorrect += 1
        else:
            numCorrect = numCorrect
    if numCorrect == number:

        #print("You win the Jackpot! All numbers matched!")
        return(numCorrect)
    else:

        #print("You got", numCorrect, "/", numbers, "correct. Better luck next time!")
        return(numCorrect)





def winStats(reps, number):
    hits = 0
    pbProb = 0
    for x in range(0, reps):
        if number == 6:
            hits = lotRand(number)[0] + hits
            pbProb = lotRand(number)[1] + pbProb
        else:
            hits = lotRand(number) + hits
    if number == 6:
        pbAvg = pbProb / reps
        avg = hits / reps
        avgHits = hits / (reps * number)
        print ("On average you will get", avg, "numbers correct and have", avgHits * 100, "percent of the numbers correct if you play", number, "numbers. The chance of a getting a PowerBall number is", pbAvg * 100,"percent. This was calculated through", reps, "repetitions.")
        return (avgHits)
    else:
        avg = hits / reps
        avgHits = hits / (reps * number)
        print ("On average you will get", avg, "numbers correct and have", avgHits * 100, "percent of the numbers correct if you play", number, "numbers. This was calculated through", reps, "repetitions.")
        return (avgHits)