'''
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''

#  myCode -> Working.
#  What SUBARRAY with size K gives us the MAXIMUM SUM
import math
def max_sub_array_of_size_k(k, arr):
    maxSum = 0
    windowStart = 0
    windowSum = 0
   
#  That is why we use an iteration here. very important. 
    for windowEnd in range(len(arr)): 
        # add the next element
       windowSum += arr[windowEnd] 

#  no need to slide if we dont hit the needed window size.
       if windowEnd >= k-1:
           # return the MAX of the Two 
        maxSum = max( maxSum, windowSum)
        #subtract element going out.
        windowSum -= arr[windowStart] 
        windowStart += 1

    return maxSum





def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()

'''
Time complexity => O(N)

Space complexity => 0(1)
'''