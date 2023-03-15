def forLoops():
    res = range(5, 22, 4)
    for num in res:
        print (num)

def pay(wage, hours):
    if hours <= 40:
        return wage*hours
    else:
        return 40 * wage + 1.5*(hours-40)*wage

def abbreviation(day):
    weekday = day[0:2]
    return (weekday)

def collision(x1, y1, r1, x2, y2, r2):
    distance = ((x2-x1)**2 + (y2-y1)**2)
    radius = (r1 + r2)**2
    if (radius >= distance):
        return True
    else:
        return False

def partition(players):
    for player in players:
        if player[0] in 'ABCDEFGHIJKLM':
            print (player)

def lastF(FirstName, LastName):
    return LastName + ', ' + FirstName[0] + '.'
    
if __name__=='__main__':
   import doctest
   print( doctest.testfile('hw2TEST.py'))
        
        
