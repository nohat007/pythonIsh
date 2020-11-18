# Program to guess the largest number of 3 arguments

# Prompt to let these idiots know whats happenin
print('Welcome to my World input 3 numbers and we will guess the largest one')
print('First num')
num1 = input()
print('Second num')
num2 = input()
print('Third num')
num3 = input()


#Function to take 3 numbers and do the work, Wow look at him go
#Takes input as string so you need to change it to ints or you get screwed, i got screwed lol
def maxOfThree(first, second, third):
    numArray = [int(first),int(second),int(third)]
    numArray = sorted(numArray)
    # test print(numArray)
    return numArray[-1]

#To let you know that we got you, we got your number
print('the largest number you put was ' + str(maxOfThree(num1, num2 , num3)))


# test maxOfThree(num1, num2 , num3)

    

