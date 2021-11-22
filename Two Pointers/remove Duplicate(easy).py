'''
Problem Statement 
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.
Example 1:
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
Example 2:
Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
'''


def remove_duplicates(arr): 
    # next_non_duplicate = 1
    # i = 1

    # while(i < len(arr)):
    #     print(arr[i], arr[i-1])
    #     if arr[i] != arr[i-1]:
    #         next_non_duplicate += 1
    #     i += 1
    # return next_non_duplicate
    
        
    #solution 2 -> working
    print(len(list(set(arr))))



#answer
def remove_duplicates(arr):
  # index of the next non-duplicate element
  next_non_duplicate = 1

  i = 1
  while(i < len(arr)):
    if arr[next_non_duplicate - 1] != arr[i]:
      arr[next_non_duplicate] = arr[i]
      next_non_duplicate += 1
    i += 1

  return next_non_duplicate

def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))

# main()


'''
Time Complexity 
The time complexity of the above algorithm will be O(N), 
where ‘N’ is the total number of elements in the given array.
Space Complexity 
The algorithm runs in constant space O(1).
'''





'''
Similar Questions #
Problem 1: Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.
Example 1:
Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].
Example 2:
Input: [2, 11, 2, 2, 1], Key=2
Output: 2
Explanation: The first two elements after removing every 'Key' will be [11, 1].
'''



def remove_element(arr, target_key):
#sort the arr
    arr.sort()    

    next_duplicate = 1
    i = 1

    while(i < len(arr)):
        if arr[i] != target_key:
            next_duplicate += 1
        i += 1
    return next_duplicate



def main():
  print("Array new length: " +
        str(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)))
  print("Array new length: " +
        str(remove_element([2, 11, 2, 2, 1], 2)))
main()

'''
Time and Space Complexity: 
The time complexity of the above algorithm will be O(N), where ‘N’ is the total number of elements in the given array.
The algorithm runs in constant space O(1).
'''