'''
Problem Statement 
Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, 
hence, we can’t count 0s, 1s, and 2s to recreate the array.
The flag of the Netherlands consists of three colors: red, white and blue; 
and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.
Example 1:
Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]
Example 2:
Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]
'''
 #my code
# def dutch_flag_sort(arr):
#     left, right = 0, len(arr)
    
#     while left <= right:

#         if arr[left ] > arr[right]:
#             arr[left], arr[right] =  arr[right], arr[left]
#             left+= 1
#         else:
#             arr[right] -= 1
#     return arr


# answer. No Working yet. Need to debug
def dutch_flag_sort(arr):

    left, i = 0,0
    right = len(arr) -1 # length in this case start from Zero. 

    while i <= right:
        if arr[i] == 0:
            arr[i], arr[left] = arr[left], arr[i] # this is a swap
            left += 1
            i += 1
        elif arr[i] == 2:
            arr[i], arr[right] = arr[right], arr[i] # this is a swap
            right -= 1
        else:
            i += 1
    return 

    

def main():
  print(dutch_flag_sort([1, 0, 2, 1, 0]))
  print(dutch_flag_sort([2, 2, 0, 1, 2, 0]))
main()



'''
Time complexity 
The time complexity of the above algorithm will be O(N) as we are iterating the input array only once.
Space complexity #
The algorithm runs in constant space O(1).
'''