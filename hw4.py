#hw4.py
#Benjamin Osborn

def vowelIndex(phrase):
    phrase = phrase.lower()
    for char in phrase:
        if char in 'aeiou':
            return phrase.index(char)
    return -1

def flipCase(word):
    ans = ''
    for char in word:
        if char in 'abcdefghijklmnopqrstuvwxyz':
            ans += char.upper()
        else:
            ans += char.lower()
    return ans
            
def palindromes(sentence):
    lstPalindromes = []
    #strip punctuation
    for punct in '.?!,:;':
        sentence = sentence.replace(punct,'')
    splitContent = sentence.split()
    for word in splitContent:
        #determine if palindrome
        if word.upper() == word.upper()[::-1]:
            lstPalindromes.append(word)
    return lstPalindromes

def squares(twoDLst):
    squareLst = []
    for intLst in twoDLst:
        for num in intLst:
            #determine if square root is a whole number
            if int(num**(1/2))**2 == num:
                squareLst.append(num)
    return len(squareLst)

def rps(p1, p2):
    if p1 + p2 == 'RS':
        return -1
    elif p1 + p2 == 'RP':
        return 1
    elif p1 + p2 == 'SR':
        return 1
    elif p1 + p2 == 'SP':
        return -1
    elif p1 + p2 == 'PR':
        return -1
    elif p1 + p2 == 'PS':
        return 1
    else:
        return 0

if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw4TEST.py'))
    
