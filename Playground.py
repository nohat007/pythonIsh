print('welcome to the number game pleae enter 2 numbers')
print('num 1')
num1 = input()
print('num 2')
num2 = input()

if num1 > num2:
    print(str(num1)+ ' is greater than ' + str(num2))
elif num2 > num1 :
    print(str(num2)+ ' is greater than ' + str(num1))
else:
    print("Both are equal")

