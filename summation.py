def summation(num1, num2):
    result = num1 + num2
    return result

print(f"The sum is {summation(20,30)}")

def multiply(num1, num2):
    result  = num1 * num2
    return result 

print(f"The product of the two number is {multiply(20,30)}")

def isOdd(num):
    if num % 2 != 0:
        return True
    else:
        return False
print(f"The number is odd: {isOdd(21)}")
print(isOdd(23))

