# hw8.py
# Benjamin Osborn

class Pizza():

    def __init__(self, size ='M', toppings = set()):
        self.s = size
        self.t = set(toppings)

    def __repr__(self):
        return f"Pizza('{self.s}',{self.t})"

    def __eq__(self, other):
        return self.s == other.s and self.t == other.t

    def setSize(self, pizzaSize):
        self.s = pizzaSize

    def getSize(self):
        return (self.s)

    def addTopping(self, plusSelf):
        self.t.add(plusSelf)

    def removeTopping(self, minusSelf):
        self.t.remove(minusSelf)

    def price(self):
        if self.s == 'S':
            pizzaPrice = 6.25 + (len(self.t)*.70)
        elif self.s == 'M':
            pizzaPrice = 9.95 + (len(self.t)*1.45)
        else:
            pizzaPrice = 12.95 + (len(self.t)*1.85)
        return pizzaPrice

def orderPizza():
    print ('Welcome to Python Pizza!')
    size = input('What size pizza would you like (S,M,L): ')
    orderedPizza = Pizza(size,set())
    while True:
        ans = input('Type topping to add (or Enter to quit): ')
        if ans == '':
            break
        else:
            orderedPizza.addTopping(ans)
    print ('Thanks for ordering!')
    print (f"Your pizza costs ${orderedPizza.price()}")
    return orderedPizza
        
    

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw8TEST.py'))
       
        
        
        

    

    
            
