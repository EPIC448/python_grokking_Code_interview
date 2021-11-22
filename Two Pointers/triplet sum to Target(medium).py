'''
Triplet Sum Close to Target (medium)
Problem Statement 
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. 
If there are more than one such triplet, return the sum of the triplet with the smallest sum.
Example 1:
Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
Example 2:
Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
Example 3:
Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
'''

def triplet_sum_close_to_target(arr, target_sum):
    triplet = []
    arr.sort()
 
    for i in range(len(arr)):

      if i > 0 and arr[i] == arr[i- 1]:
       continue
    
    search_pair(arr ,target_sum,   i+1,  triplet)
    
    return triplet


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







def main():
  print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()


'''
Time complexity 
Sorting the array will take O(N* logN)O(N∗logN). Overall 
searchTriplet() will take O(N * logN + N^2), 
which is asymptotically equivalent to O(N^2).
Space complexity 
The space complexity of the above algorithm will be O(N) which is required for sorting.
'''