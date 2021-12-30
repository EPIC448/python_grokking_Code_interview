# Add up all the number in the List together
'''

list = [2,1,3,4,]
listTotal = 0
for i in range(len(list)):
     listTotal  += list[i]
print(listTotal)
'''


'''
# Sum Up all Prime Numbers

#  What is a PRIME NUMBER = A prime number is defined as a number greater than one and having only two 
# divisors, one and itself. For example, 2 is a prime number because it's only divisible by one and two.
#  This  solution below is correct. and I need to Resolve the one above. for Clearity.
for num in range(2,10):
    prime = True
    for i in range(2,num):
        print("This are what I means here"+ str(i))
        if (num%i==0):
            prime = False
    if prime: 
       print("Prime remains" + str(prime))
       print ("finale result" + str(num))
'''

#  Taking in an array of inputs, return the suma of even and Numbers.
#  Note: I am adding to method in 1. 

def evenOddSums(n):
    evenNumTotal = 0
    oddNumTotal = 0
    #  Iteration
    for num in range(0, n):
    #  Even number % 2 == 0
      
        if num % 2 == 0:
            evenNumTotal += num
    # #  Else it is an Odd Number
        else:
            oddNumTotal += num
    return [
        "the is the total for EvenNum "  + str(evenNumTotal), 
        "the is the total for OddNum " + str(oddNumTotal)
        ]


#   For Function 2...

    #  Even number % 2 == 0
      
    #     if arr[num] % 2 == 0:
    #         evenNumTotal += arr[num]
    # #  Else it is an Odd Number
    #     else:
    #         oddNumTotal +=arr[num]
    # return [
    #     "this is the total for EvenNum "  + str(evenNumTotal), 
    #     "this is the total for OddNum " + str(oddNumTotal)
    #     ]
n =100
print(evenOddSums(n))
#  Function 2, print(evenOddSums([50, 60, 60, 45, 71]) )