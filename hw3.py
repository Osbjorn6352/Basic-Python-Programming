#HW3.PY
#Benjamin Osborn
#Collaborators: Sherelyn Saceda, Purva Jay Dovaria


def cheer(teamName):
    spellCaps = teamName.replace('',' ').upper()[1:]
    chant = "How do you spell winner?\nI know, I know!\n{}!\nAnd that's how you spell winner!\nGo " + (teamName) + '!'
    print (chant.format(spellCaps))

def vowelCount(phrase):
    aCount = phrase.upper().count('A')
    eCount = phrase.upper().count('E')
    iCount = phrase.upper().count('I')
    oCount = phrase.upper().count('O')
    uCount = phrase.upper().count('U')
    #insert counts into string
    result = 'a, e, i, o, and u appear, respectively, ' + str(aCount)+ ', ' + str(eCount) + ', ' + str(iCount) + ', ' + str(oCount) + ', ' + str(uCount) + ' times.'
    print (result)

def crypto(file):
    with open(file) as infile:
        print (infile.read().replace('secret','xxxxxx'))

def links(htmlFile):
    with open(htmlFile) as infile:
        return infile.read().count('</a>')

def duplicate(file):
    with open(file) as infile:
        modContents = infile.read().upper()
        #strip punctuation
        for punct in '.?!,:;':
            modContents = modContents.replace(punct, '')
        #make a list
        splitContent = modContents.split()
        #search the list for duplicates
        for word in splitContent:
            if splitContent.count(word)>1:
                return True
        return False
        
if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw3TEST.py'))
    
