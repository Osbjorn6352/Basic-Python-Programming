#hw5.py
#Benjamin Osborn

def doubleVowel(word):
    for i in range(len(word)-1):
        if word[i] in 'aeiouAEIOU' and word[i+1] in 'aeiouAEIOU':
            return True
    return False

def numPairs(target, numLst):
    # 0 - create an accumulator
    count = 0
    # 1 - iterate over the indices
    for i in range(len(numLst)):
        # 2 - determine whether the number added with any number gives target number
        for j in range(len(numLst)):
            #make sure you only count numbers once by only counting if j>i
            if j>i and numLst[i] + numLst[j] == target:
                count += 1
    return count
    
def hideShow(instring, maskstring):
    newString = ''
    for i in range(len(maskstring)):
        if maskstring[i] == '0':
            newString += '#'
        else:
            newString += instring[i]
    return newString

def clean(string):
    while string[0] in ' \n\t':
        string = string[1:]
    while string [-1] in ' \n\t':
        string = string[:-1]
    return string

def sequence(num):
    print(num)
    while num != 1:
        if num%2 == 0:
            num = num//2
        else:
            num = num + 1
        print (num)
        

if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw5TEST.py'))
