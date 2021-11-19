'''
Problem Statement 
Given an array of characters where each character represents a fruit tree, you are given two(2) baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.
Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''
# Code was corrected using  Orginal answer ... some worth talking

'''

def fruits_into_baskets(fruits):
    longest_window = 0
    window_start = 0
    dict_frequency = {}

    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        
        if right_fruit not in dict_frequency:
            dict_frequency[right_fruit] = 0
        else:
            dict_frequency[right_fruit] += 1

# shrink the sliding window, until we are left with '2' fruits in the Fruits in frequency dictionary
# We use While so we can keep  Compare the Length of the "dic_frequency" .. compared to IF.. else that just run once.
        while (len(dict_frequency) > 2):
            left_fruit = fruits[window_start]
            # if the element already exsit in the Dict and it is greater than 2
            dict_frequency[left_fruit] -= 1
            # if the character is Zero. we can remove it.
            if dict_frequency[ left_fruit] == 0:
                del dict_frequency[  left_fruit]
            window_start += 1  # shrinks the window
        longest_window = max(longest_window, window_end - window_start + 1)
    return longest_window
'''

# answer

    
def fruits_into_baskets(fruits):
    window_start = 0
    max_length = 0
    fruit_frequency = {}

    #try to extend the range [window_start, window_end]
    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]

        if right_fruit not in fruit_frequency:
            fruit_frequency[fruits[right_fruit]] = 0
        else:
            fruit_frequency[fruits[right_fruit]] += 1

    # shrink the sliding window, until we are left with '2' fruits frequency dictionary
    # We can only collect 2 Fruits. 1 for each basket. SO when we get more than the same type of fruits,
    # we move the window_start
        while(len(fruit_frequency) > 2):
            left_fruit = fruits[window_start]
            fruit_frequency[left_fruit] -= 1

            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            window_start += 1 # shrink window
        max_length = max(max_length, window_end - window_start + 1)
    return max_length




def main():
    print("Maximum number of fruits: " +
          str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " +
          str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
