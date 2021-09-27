# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertion_sort_list(self, head: ListNode) -> ListNode:
        unsorted = head.next            # First unsorted node in linked list
        previous_unsorted = head

        while unsorted:
            target = head               # Target position for insertion
            previous_target = None
            is_inserted = False

            while (not is_inserted and target != unsorted):
                if unsorted.val >= target.val:
                    previous_target = target
                    target = target.next
                    continue

                elif previous_target:
                    previous_target.next = unsorted

                else:
                    head = unsorted

                previous_unsorted.next = unsorted.next
                next_unsorted = unsorted.next
                is_inserted = True
                unsorted.next = target


            if is_inserted:
                unsorted = next_unsorted

            else:
                previous_unsorted = unsorted
                unsorted = unsorted.next

        return head

    def display(self, head):
        node = head
        while node:
            print(node.val, end='')
            node = node.next
        print('')


# Complexity Analysis
# Time: O(n^2)
# Space: O(1)

# Tests
S = Solution()

node_3 = ListNode(3)
S.display(S.insertion_sort_list(node_3))  # [3]

node_3 = ListNode(3)
node_1 = ListNode(1, node_3)
S.display(S.insertion_sort_list(node_1))  # [1, 3]

node_3 = ListNode(3)
node_1 = ListNode(1, node_3)
node_2 = ListNode(2, node_1)
S.display(S.insertion_sort_list(node_2))  # [2, 1, 3]

node_3 = ListNode(3)
node_1 = ListNode(1, node_3)
node_2 = ListNode(2, node_1)
node_4 = ListNode(4, node_2)
S.display(S.insertion_sort_list(node_4))  # [4, 2, 1, 3]

node_5 = ListNode(5)
node_7 = ListNode(7, node_5)
node_6 = ListNode(6, node_7)

S.display(S.insertion_sort_list(node_6))  # [5, 7, 6]
