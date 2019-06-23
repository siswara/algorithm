import math

def karatsuba(input0, input1):
    ret = 0
    
    #implement recursive
    #base case number is 2 digit
    #if (len(input0) <= 3 or len(input1) <= 3): #base case
    if input0 == '' and input1 == '':
        return 0
    elif (len(input0) <= 2 or len(input1) <= 2): #base case
        #print ('input0 : ' + input0)
        #print ('input1 : ' + input1)
        ret = long(input0) * long(input1)
        return ret
    

    #recursive function
    input0NthPower = int(len(input0))
    input1NthPower = int(len(input1))
    nthPower = 0 # initialize var
    nthPower = max(input0NthPower, input1NthPower)

    if (input0NthPower%2 == 1) or (input1NthPower%2 == 1):
       nthPower = nthPower - 1
    
    #print('input0NthPower : ' + str (input0NthPower))
    #print('input1NthPower : ' + str (input1NthPower))
    #print('nthPower : ' + str (nthPower))
    digitA = input0[0:input0NthPower - nthPower/2]
    digitB = input0[input0NthPower - nthPower/2:input0NthPower]
    digitC = input1[0:input1NthPower - nthPower/2]
    digitD = input1[input1NthPower - nthPower/2:input1NthPower]
    
    #AC multiplication
    firstSubResult = karatsuba(digitA, digitC) 
    firstResult = firstSubResult * (10**nthPower)#int(pow(10,nthPower))

    #BD multiplication
    secondSubResult = karatsuba(digitB, digitD)
    secondResult = secondSubResult 

    #last multiplication step
    digitAB = long(digitA) + long(digitB)
    digitCD = long(digitC) + long(digitD)
    thirdSubresult = karatsuba(str(digitAB), str(digitCD))
    thirdResult = (thirdSubresult - secondSubResult - firstSubResult) * (10**(nthPower/2))#int(pow(10, nthPower/2))
    ret = firstResult + secondResult + thirdResult
    
    return ret

#call fuction
num0 = '3141592653589793238462643383279502884197169399375105820974944592'
num1 = '2718281828459045235360287471352662497757247093699959574966967627'

print(num0 + ' * ' + num1 + ' = ' )
print(str(long(karatsuba(num0,num1))))

#test cases
# num0 = '100779'
# num1 = '531718'
# print(num0 + ' * ' + num1 + ' = ' + format(karatsuba(num0,num1),'10.0f'))

# num0 = '184559'
# num1 = '564155'
# print(num0 + ' * ' + num1 + ' = ' + format(karatsuba(num0,num1),'10.0f'))

# num0 = '143291'
# num1 = '860264'
# print(num0 + ' * ' + num1 + ' = ' + format(karatsuba(num0,num1),'10.0f'))

# num0 = '420224'
# num1 = '735225'
# print(num0 + ' * ' + num1 + ' = ' + format(karatsuba(num0,num1),'10.0f'))

# num0 = '47102997'
# num1 = '95062499'
# print(num0 + ' * ' + num1 + ' = ' + str(long(karatsuba(num0,num1))))

# num0 = '70608127'
# num1 = '84416766'
# print(num0 + ' * ' + num1 + ' = ' + str(long(karatsuba(num0,num1))))

# num0 = '14219'
# num1 = '7427'
# print(num0 + ' * ' + num1 + ' = ' + str(long(karatsuba(num0,num1))))