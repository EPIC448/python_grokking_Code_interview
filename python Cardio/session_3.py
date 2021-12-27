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


