'''

https://www.youtube.com/watch?v=yOzXms1J6Nk   best sloution

Problem Challenge 1
Palindrome LinkedList (medium)
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.
Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.
Example 1:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true
Example 2:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false
'''


class Node:
    def __int__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):

 # helper Code
    if head is None or head.next is None:
        return True

    # find the middle of the LinkedLIist
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    # reverse the second Half,and Use for later..
    head_second_half = reverse(slow)
    copy_head_second_half = head_second_half

    # compare the first and the second Half
    while (head is not None and head_second_half is not None):
        if head.value != head_second_half.value:
             break  # not a Palindrome

    head = head.next
    head_second_half = head_second_half.next

    # revert the revers of the Second half
    reverse(copy_head_second_half)

    if head is None or head_second_half is None:  # if both halves match
        return True

    return False


# reverse the  LinkedinList.
def reverse(head):
    prev = None
    while (head is not None):
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()


#  Better shorter solution here.


'''
Time complexity 
The above algorithm will have a time complexity of O(N) where ‘N’ is the number of nodes in the LinkedList.
Space complexity 
The algorithm runs in constant space O(1).
'''



