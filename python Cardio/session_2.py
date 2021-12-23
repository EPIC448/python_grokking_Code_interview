#  Longest Word

def getLongestWord (str):
    longestWord = max(str.split(), key=len)
    print(longestWord)


# print(getLongestWord("force be with you there is something new"))

'''
#  note: Slice in Python does nor Directly use the word slice... Is uses the notation.

def chuckArray(arr, size):
    index = 0
    chuncked_arr = []
    while index < len(arr):
        chuncked_arr.append(arr[index : size + index])
        index += size
    return chuncked_arr


print (chuckArray([1,2,3,4,5,6,7], 4))

'''

# note that I skip the Flatten List here. Need a little work.

def isAnagram(str1, str2):
    str1 = str1.replace(" ", "")

    for i in range(len(str1)):
    
       str1 = str1[::-1]
       if (str1 == str2):
            return (True)
       else:
            return (False)


   
        # if(str1[i] == reversedString):
        #     return True
        # else:
        #     return False
        


print(isAnagram("dirty Room", "dormitory")) # false// 