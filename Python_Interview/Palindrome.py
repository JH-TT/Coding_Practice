class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = [] # q : Deque = collections.deque() 를 이요해서 더 빠르게 수행하도록 할 수 있다.
        
        if not head : # 비어있는 리스트라면 성립.
            return True
        
        node = head
        
        while node is not None:
            q.append(node.val)
            node = node.next
            
        while len(q) > 1:
            if q.pop(0) != q.pop(): # 가장끝과 가장 앞을 꺼내서 다르면 False.
            # deque로 했으면, q.pop(0)이 q.popleft()가 되어 시간복잡도가 O(1)이 된다.
                return False
            
        return True # while문을 통과한건 짝이 다 맞는다는 소리 이므로 True리턴.

# 1번째 테스트 케이스 (1->2->2->1) : True
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(2)
a4 = ListNode(1)

a1.next = a2
a2.next = a3
a3.next = a4

answer = Solution()
if answer.isPalindrome(a1):
    print("성공")
else:
    print("실패")

# 2번째 테스트 케이스 (1->2) : False
a1 = ListNode(1)
a2 = ListNode(2)

a1.next = a2

answer = Solution()
if answer.isPalindrome(a1):
    print("성공")
else:
    print("실패")

# 런너로 풀이.
# fast와 slow가 주어진다.
# 이 둘은 head에서 시작하고, fast는 2칸씩, slow는 한 칸씩 이동한다.
# 그러면서 역순으로 연결리스트 rev를 생성하는 로직을 slow앞에 덧붙인다.
# 예를 들면 1 2 3 2 1 이라하면, rev는 2 1 none 순서고, slow는 3 오른쪽인 2를 가리키고 있는 중이다.
# 이때 서로 값이 같은지 비교하면서 next를 한다.

def isPalindrome(self, head: ListNode) -> bool:
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev