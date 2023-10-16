# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def create_linked_list(vals):
    dummy = ListNode()
    current = dummy

    for val in vals:
        current.next = ListNode(val)
        current = current.next

    return dummy.next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:



vals = [1, 4, 3, 2, 5, 2]
linked_list = create_linked_list(vals)

# Test Code
solution = Solution()
#result = solution.search([6, 7, 8, 9, 0, 0, 1, 1, 2, 3, 4, 5, 6], 8)
result = solution.partition(linked_list, 3)


# Print the result
print("Result:",result)
