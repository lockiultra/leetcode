class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.intToList(self.listToInt(l1) + self.listToInt(l2))

    def listToInt(self, list_node: ListNode) -> int:
        tmp = list_node
        num = ''
        while tmp is not None:
            num += str(tmp.val)
            tmp = tmp.next
        return int(num[::-1])

    def intToList(self, number: int) -> ListNode:
        num_str = str(number)[::-1]
        tmp = ListNode(num_str[0])
        if len(num_str) > 1:
            for x in num_str[1:]:
                self.addNode(tmp, int(x))
        return tmp
    
    def addNode(self, node, val):
        tmp = node
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = ListNode(val)
        