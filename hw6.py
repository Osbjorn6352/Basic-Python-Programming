# hw6.py
# Benjamin Osborn

def interleaved(numLst1, numLst2):
    ans = []
    i = 0
    j = 0
    while i in range(len(numLst1)) and j in range(len(numLst2)):
        if numLst2[j] < numLst1[i]:
            ans.append(numLst2[j])
            j += 1
        else:
            ans.append(numLst1[i])
            i += 1
    for num in numLst1[i:]:
        ans.append(num)
    for num in numLst2[j:]:
        ans.append(num)
    return ans

def primeFac(integer):
    n = integer
    ans = []
    candidate = 2
    while n != 1:
        if n % candidate == 0:
            n = n/candidate
            ans.append(candidate)
        else:
            candidate += 1
    return ans

def piggyBank(coins):
    coinCounts = {'Q':0, 'D':0, 'N':0, 'P':0}
    for coin in coins:
        if coin == 'Q':
            coinCounts['Q'] += 1
        elif coin == 'D':
            coinCounts['D'] += 1
        elif coin == 'N':
            coinCounts['N'] += 1
        else:
            coinCounts['P'] += 1
    totalValue = coinCounts['Q']*25 + coinCounts['D']*10 + coinCounts['N']*5 + coinCounts['P']
    return (coinCounts, totalValue)

def craps():
    import random
    pips = 0
    d1 = random.randrange(1,7)
    d2 = random.randrange(1,7)
    pips = d1 + d2
    if pips in (7,11):
        return 1
    elif pips in (2,3,12):
        return 0
    else:
        d1 = random.randrange(1,7)
        d2 = random.randrange(1,7)
        pips2 = d1 + d2
        while pips2 != 7 and pips2 != pips:
            d1 = random.randrange(1,7)
            d2 = random.randrange(1,7)
            pips2 = d1 + d2
        if pips2 == 7:
            return 0
        else:
            return 1     

def testCraps(numGames):
    crapsTotalValue = 0
    for num in range(numGames):
        if craps() == 1:
            crapsTotalValue += 1
    crapsAvg = crapsTotalValue/numGames
    return crapsAvg
    
        
    
if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw6TEST.py')) 
