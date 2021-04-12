class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val): # l1이 None이거나 l2가 있고, l1의 값이 l2의 값보다 크면 교환.
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2) # 다음으로 l1.next와 l2를 비교하러 감.
        
        return l1