# randInt() returns a random integer between 0 to 100
import random
def randInt():
    print(int(random.random()*100))
randInt()
# randInt(max=50) returns a random integer between 0 to 50
import random
def randInt2():
    print(int(random.random()*50))
 randInt2()

# randInt(min=50) returns a random integer between 50 to 100
import random
def randInt3():
    values = list(range(50,100))
    print(int(random.random(values))
randInt3()

# randInt(min=50, max=500) returns a random integer between 50 and 500

import random
def randInt4():
    values = list(range(50,500))
    print(random.choice(values))
randInt4()

import random
def function():
    print(round(random.random()*10+5))
function()
# MAX 15
# MIN 5

import random
def randInt(max,min):
    print(round(random.random()*max+min))
randInt(50,50)
# max:100
# min:50
