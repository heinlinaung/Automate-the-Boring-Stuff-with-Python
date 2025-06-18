# Binary Operator ' and , or '

# 'and' - checking False exists 
## True and True -> True
## True and False -> False 
## False and True -> False 
## False and False -> False 


# 'or' - checking True exists
##  True or True -> True    
##  True or False -> True 
##  False or True -> True
##  False or False -> False 
#######

# Unary operator 'not'
# 'not' - convert to opposite
## not True -> False
## not False -> True 
#######


# Code Block
name = 'hein'
password = 'abcdpwd'
if name == 'hein':
    print('hello hein')
    if password == 'abcdpwd': 
        print('Access granted!')
    else:
        print('wrong password')


## if vs whiel loop
## if loop, proceed to next
spam = 0
if spam < 5:
    print('hello world')
    spam = spam + 1


## while jump back to start after loop
wspam = 0
while wspam < 5:
    print('hello while world')
    wspam = wspam + 1

## annoying while loop (will ask until you type 'your name' as the value) 
name = ''
while name != 'your name':
    print('Please type your name')
    name = input()
print('thx u')

## while loop with break statement same workflow but diff syntax
while True:
    print('Please type my name')
    myname = input() 
    if myname == 'my name':
        break
print('thannnnksss')

print('what is your name')
aliceName=input()
print('How old are you?')
aliceAge=input()
if aliceName=='Alice' and int(aliceAge) == 20:
    print('Hi, Alice')
elif int(aliceAge) < 12:
    print('You not not alice, kiddo')
else :
    print('who are you?')


print('let\'s count 1 to 5')
for i in range(5):
    print('Count ',i+1)


print('let\'s count with while loop')
whilecounter=0
while whilecounter<5:
    print('while count ->',whilecounter+1)
    whilecounter=whilecounter+1

print('let\s count from 10 to 15')
for i in range(10,16):
    print('counter =>', i)

print('let\s count even numbers')
for i in range(0,11,2):
    print('counter ->',i)


print('let\s import random lib and check')
import random
for i in range(5):
    print(random.randint(1,10))
