def div42By(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('My g...... you tried to divide by zero man SMH')
    
print(div42By(2))
print(div42By(12))
print(div42By(0))
print(div42By(1))
