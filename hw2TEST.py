# hw2TEST.py


>>> from hw2 import *

##### forLoops #####

>>> forLoops()
5
9
13
17
21
>>>

##### pay ######

>>> pay(10,10)
100
>>> pay(10,45)
475.0
>>> pay(10,10)==100 # check return vs. print
True
>>> pay(10,35)==350 # check return vs. print
True
>>> pay(10,45)==475.0 # check return vs. print
True
>>> pay(13.25,40)==530.0 # check return vs. print
True

##### abbreviation ######


>>> abbreviation('Tuesday')
'Tu'
>>> abbreviation( 'Monday' )=='Mo' # check return vs. print
True
>>> abbreviation( 'Wednesday' )=='We' # check return vs. print
True
>>> abbreviation( 'Sunday' )=='Su' # check return vs. print
True

##### collision ######


>>> collision(0,0,3,0,5,3)
True
>>> collision(0,0,1.4,2,2,1.4)
False
>>> collision(0,0,2,5,0,3)
True
>>> [collision(0,0,3,0,5,3), collision(0,0,1.4,2,2,1.4), collision(0,0,2,5,0,3)]  # return not print
[True, False, True]

##### partition ######

>>> partition(['Eleanor','Evelyn','Sammy','Owen','Gavin'])
Eleanor
Evelyn
Gavin
>>> partition(['Xena','Sammy','Owen'])
>>> partition(['April','Margaret','Frances','Jill'])
April
Margaret
Frances
Jill

##### lastF ######


>>> lastF('George','Washington')
'Washington, G.'
>>> lastF('Albert','Camus')
'Camus, A.'
>>> lastF('George','Washington')=='Washington, G.' # check return vs. print
True
>>> lastF('Albert','Camus')=='Camus, A.' # check return vs. print
True
>>> lastF('Hilary','Clinton')=='Clinton, H.' # check return vs. print
True
