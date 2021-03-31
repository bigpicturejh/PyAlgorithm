class ListNode:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next
    
    def printAll(self):
        while self:
            print(self.val, end=' ')
            self=self.next

class Solution:
    # def addTwoList(self, l1:ListNode, l2:ListNode) -> ListNode: 
    def revList(self, l1:ListNode,) -> ListNode: 
        node=l1
        rev=None

        while node:
            # next, node.next= node.next, rev
            # rev, node = node, next

            real_next=node.next
            node.next=rev
            rev=node
            node=real_next

        return rev

solution=Solution()
l1_4=ListNode(5)
l1_3=ListNode(4, l1_4)
l1_2=ListNode(3, l1_3)
l1_1=ListNode(2, l1_2)
l1_0=ListNode(1, l1_1)

print('l1 list is : ', end=" ")
l1_0.printAll()

result=solution.revList(l1_0)
print('result is : ', end= " ")
result.printAll()


