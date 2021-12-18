'''
Problem Statement 
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.
Example 1:
Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
Example 2:
Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:
Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
'''
#Length of SMALLEST SUBARRAY that it SUM is equal or greater then S

#mycode
import math
def smallest_subarray_with_given_sum(s, arr):
    min_length = math.inf
    windowSum = 0
    windowStart = 0

#  iteration over the giving arr
#  add up the Current window Sum

#  Keep adding to window till we hit a target S

    for windowEnd in range(0, len(arr)):
     windowSum += arr[windowEnd] #the numbers really add up here. take a note of that.

  #  shrink window till it is smaller then S
     while windowSum >= s:
       print(arr[windowEnd], arr[windowStart] +1) # this are indices

       min_length = min(min_length, windowEnd - windowStart + 1 )
       windowSum -= arr[windowStart]
       windowStart += 1

    if min_length == math.inf:
      return 0
    
    return min_length



    '''  Leetcode Solution
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#        Best Sliding windown explanition [anthony Chao]-- https://leetcode.com/problems/minimum-size-subarray-sum/discuss/277445/Python-Sliding-Window-Approach-(with-comments)
        min_length = math.inf
        windowStart = 0
        window_sum = 0
       
        for windowEnd in range(len(nums)):
            window_sum += nums[windowEnd]
            
            
            while window_sum >= target:
                min_length = min(min_length, windowEnd - windowStart + 1)
                window_sum -= nums[windowStart]
#                 Code was not passing because I didnt add the "+= 1" i only did + 1
                windowStart += 1

#               Change solution here.
        return min_length if min_length != math.inf else 0
#         # print(min_length)


 Leet code Author Authony solution using MaxSIze
 maxsize --- attribute of the sys module fetches the largest value a variable of data type Py_ssize_t can store. It is the Python platform's pointer that dictates the maximum size of lists and strings in Python
from sys import maxsize
   
def minSubArrayLen(s, nums):
	res = maxsize
	left, total = 0, 0
	
	for i in range(len(nums)):
		total += nums[i]
		while total >= s:
			res = min(res, i - left + 1)
			total -= nums[left]
			left += 1
	
	return res if res != maxsize else 0
    
    
    '''

#answer   


# import math

# def smallest_subarray_with_given_sum(s, arr):
#   window_sum = 0
#   min_length = math.inf
#   window_start = 0

#   for window_end in range(0, len(arr)):
#     window_sum += arr[window_end]  # add the next element
#     # shrink the window as small as possible until the 'window_sum' is smaller than 's'
#     while window_sum >= s:
#       min_length = min(min_length, window_end - window_start + 1)
#       window_sum -= arr[window_start]
#       window_start += 1
#   if min_length == math.inf:
#     return 0
#   return min_length

def main():
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
  # print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
  # print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))

main()


'''
Time Complexity 
The time complexity of the above algorithm will be O(N). 
The outer for loop runs for all elements and the inner while loop processes each element only once, therefore the time complexity of the algorithm will be O(N+N) which is asymptotically equivalent to O(N).

Space Complexity 
The algorithm runs in constant space O(1).
'''