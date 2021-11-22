
'''
 pre-requirment on leetcode
  2 Sum and 2 SUM 2

   Best explanation: https://www.youtube.com/watch?v=jzZsG8n2R9A

Explanation -> https://www.youtube.com/watch?v=f6YqGTpFKig&t=198s
 Need to learn and research



Problem Statement 
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
Example 1:
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:
Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.

BRUTE FORCE
Running a 3 nested Loop O(n ^3)

ALTERNATIVE
 TWO pointer approach, we need to SORT the array
 Goal is X + Y + Z = 0  also equal  Y + Z = -X

NOte: Simialar to  PAIR with a Target SUM!!!

> Instead of checking if we have a pair with SUM 0, we can check if we have a pair which SUM to -X!!
> We need to handle Cases of Duplicate. 
'''


''' 
 
'''

# use a Pair Two Skeleton , then Fill them in  as Needed. Note: I want to See if y + z = -x

def search_triplets(arr):
    triplets =[]
    arr.sort()

    for i in range(len(arr)):  # iteration over the Array
        if i > 0 and arr[i] == arr[i -1]: # Make sure I is greated then 0 && Skip duplicates
            continue # skip on to the next Loop
        search_pair(arr, -arr[i], i + 1, triplets) # Else search for the Pairs.

        return triplets

# this is what I need to learn to build

def search_pair(arr, target_sum, left, triplets):
    right = len(arr) -1

    while(left < right):
        currentSum = arr[left] + arr[right]
        
        if target_sum == currentSum:
            triplets.append([arr[left], arr[right], -target_sum])
            left += 1 # needed help
            right -=1 # Needed Help
        
         # used Help In this section..... Help use aviod duplicates.
       
            while left < right and arr[left] == arr[left -1]:
                left += 1 # skip same element to aviod duplicate Triplets.
            
            while left < right and arr[right] == arr[right + 1]:
                right -= 1 # skip same element to aviod duplicate Triplets.


        elif target_sum > currentSum:

            left += 1 # need to pair with a smaller Sum. 
        else: 
            right -=1 # need to Pair with a Larger Sum
        
      
'''  Answer
def search_triplets(arr):
  arr.sort()
  triplets = []
  for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
      continue
    search_pair(arr, -arr[i], i+1, triplets)

  return triplets


def search_pair(arr, target_sum, left, triplets):
  right = len(arr) - 1
  while(left < right):
    current_sum = arr[left] + arr[right]
    if current_sum == target_sum:  # found the triplet
      triplets.append([-target_sum, arr[left], arr[right]])
      left += 1
      right -= 1
      while left < right and arr[left] == arr[left - 1]:
        left += 1  # skip same element to avoid duplicate triplets
      while left < right and arr[right] == arr[right + 1]:
        right -= 1  # skip same element to avoid duplicate triplets
    elif target_sum > current_sum:
      left += 1  # we need a pair with a bigger sum
    else:
      right -= 1  # we need a pair with a smaller sum


'''


'''
  Redo off heart
   # need this part, but was not needed for the code.  
def search_pair(arr, target_sum, left, triplet):
  right = len(arr) -1

  while(left < right):
     currentSum = arr[left] + arr[right]

     if currentSum == target_sum:
       triplet.append([-target_sum, arr[left], arr[right]])
       left +=1
       right -=1

       while (left < right) and arr[left] == arr[left  -  1]:
         left += 1
       while(left < right) and arr[right] == arr[right + 1]:
          right -=1


     elif currentSum > target_sum:
       right -=1
     else:
        left +=1


'''




def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))


main()


'''
Time complexity 
Sorting the array will take O(N * logN).

The searchPair() function will take O(N). 
As we are calling searchPair() for every number in the input array, 
this means that overall searchTriplets() will take O(N * logN + N^2), which is asymptotically equivalent to O(N^2).

Space complexity 
Ignoring the space required for the output array, 
the space complexity of the above algorithm will be O(N) which is required for sorting.
'''