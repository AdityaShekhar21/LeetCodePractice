1class Solution:
2    def reverseBetween(self, head, left: int, right: int):
3        if not head or left == right:
4            return head
5
6        dummy = ListNode(0)
7        dummy.next = head
8        prev = dummy
9
10        for _ in range(left - 1):
11            prev = prev.next
12
13        curr = prev.next
14
15        for _ in range(right - left):
16            next_node = curr.next
17            curr.next = next_node.next
18            next_node.next = prev.next
19            prev.next = next_node
20
21        return dummy.next
22