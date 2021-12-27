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

'''

# note that I skip the Flatten List here. Need a little work.
# All parts working
def isAnagram(str1, str2):
    if(sorted(str1)== sorted(str2)):
        print(str1, str2)
        print("This is anagram, True")
    else:
        print("not an anagram")
    
    #    str1 = str1[::-1]
   

print(isAnagram("lsient", "lintes")) # false// 
'''

#  Note, skipped the one that had the Letter change in this session_2