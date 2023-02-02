# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1number = ""
        l2number = ""
        dummy = cur = ListNode(0)

        while (l1 != None):
            l1number = str(l1.val) + l1number
            l1 = l1.next
        
        print(l1number)
        
        
        while (l2 != None):
            l2number = str(l2.val) + l2number
            l2 = l2.next
        
        print(l2number)
        
        total = int(l1number) + int(l2number)
        total = str(total)

        print(total)

        for element in reversed(total):
            cur.next = ListNode(int(element))
            cur = cur.next
        
        return dummy.next
