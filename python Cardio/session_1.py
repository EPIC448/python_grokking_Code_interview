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

# Validate a isPalindrome

def  isPalindrome(str):
    stringLength= len(str)
    # using Slicing here. Create slice that start length of the string and end at zer0 
    reversed =str[stringLength:: -1]
    if reversed == str:
        return True
    else:
        return False


print(isPalindrome('racecar'))  #=> "racecare" should give us true

