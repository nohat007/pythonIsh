#Guess the number game
import random

print('Hi welcome to my guessing game, what is your name?: ')
name = input()
#print(name)
print('Sweet ' + name + ' You are going to pick a number between 1 and 20: ')

aiNum = random.randint(1,20)


for i in range(1,7):
    print('Take a Guess....')
    myNum = input()
    myNum = int(myNum)
    
    if myNum < aiNum :
        print('Too Low')
        
    elif  myNum > aiNum:
        print('Too High')
        
    else :
        break
       # print('The number are equal,it took you ' + str(i) + ' tries')

       


if myNum == aiNum:
    print('Congrats you guessed the number in '  + str(i) + ' tries')
else :
    print('You\'ve reached your limit, the number I chose was ...... ' + str(aiNum))
        

    
        
    
    

