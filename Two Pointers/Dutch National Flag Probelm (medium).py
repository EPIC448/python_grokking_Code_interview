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


 APPROACH:
  Use a "while LOOP" as long as i is less < righto
    Check that If CURRENT "i" is "0" => move to the "LEFTside" of our LEFT POINTER
    Check that If CURRENT "i" is "2" => move to the "RIGHTside" of our RIGHT POINTER
    the "1" fall naturally between in place



'''
# my code... Fixed with Help from Answer  code. 

def dutch_flag_sort(arr):
    left, i = 0, 0
    right = len(arr) -1
    
    while i <=  right:
        if arr[i] == 0:
            arr[i], arr[left] = arr[left], arr[i]  # we swap because we are changing in place.
            left +=1
            i += 1
        elif arr[i] == 2:
             arr[i], arr[right] = arr[right], arr[i]
             right -= 1
        else:
            i += 1
    return arr
  




''' 
answer.  Working Properly.
Break down
while Iterating
> move all Zero to the left of the LEFT pointer
>Move all TWO to the RIGght of the RIGHT POINTER.
> ALL ONES will be between the LEFT and The RIGHT POINTER

Using the exmaple above
Input: [1, 0, 2, 1, 0]
Output: [0 0  "L" 1 1  "R" 2]


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
            i += 1 # by deflaut > 1 just fall in between 0 and 2
    return arr
'''


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
