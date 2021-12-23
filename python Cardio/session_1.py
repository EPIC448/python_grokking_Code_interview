# Reverse a String
# ex. reverseString('hello') === 'olleh'
#  Python does not have an inbuilt reverse method. so to fix that
#  Reverse a String
stringSample = "Hello"
reversed= ''.join(reversed(stringSample))
# print(reversed) # =>[olleh]

listSample = [1,2,3,4,5]
listSample.reverse()
# print(listSample) # => [5,4,3,2,1]

# Reverse a number
num = [3,2,1,2,3]
num.reverse()
# print(num)


# Validate a isPalindrome

def  isPalindrome(str):
    stringLength= len(str)
    # using Slicing here. Create slice that start length of the string and end at zero 
    reversed =str[stringLength:: -1]
    if reversed == str:
        return True
    else:
        return False


# print(isPalindrome('racecar'))  #=> "racecare" should give us true

# Return a string with the first letter of every word capitalized
# ex. capitalizeLetters('i love javascript') === 'I Love Javascript'

def  capitalizeLetters(str):
    return str.title()
    
# print(capitalizeLetters("i love bodybuilding so Much ereafs"))


#  find the MaxCharacter in a string # Resolve this. 
# Using Method Counter. using collections.Counter() + max() to get #Maximum frequency character in string
'''

from collections import Counter
def maxCharacter(str):
    res = Counter(str)
    res = max(res, key = res.get)
    print(res)


#  Using a Object to see if that letter already exsist
def maxCharacter(str):
    all_freq = {}
    for i in str:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] =1
    print(all_freq)
    res = max(all_freq, key=all_freq.get)
    print(res)


print(maxCharacter('ajavascrijptaya'))

'''

'''
# FizzBuZZ
Write a program that prints all the numbers from 1 to 100. 
 For multiples of 3, instead of the number, print "Fizz", 
 for multiples of 5 print "Buzz".For numbers which are multiples of both 3 and 5, print "FizzBuzz".
# .. Working

def fizzBuzz(n):
    if n < 1:
        return 1
    for element in range(n):
        if element % 3 == 0 and element % 5 == 0:
            print('fizzbuzz')
            continue
        elif element % 3 == 0:
            print('Fizz')
            continue
        elif element % 5 == 0:
            print('Buzz')
            continue
        print(element)

print(fizzBuzz(15))

'''
