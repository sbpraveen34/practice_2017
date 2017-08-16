def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    univ = set()
    tempA = headA
    tempB = headB
    while(tempA):
        univ.add(id(tempA))
        tempA = tempA.next

    while(tempB):
        if id(tempB) in univ:
            return tempB.data
        tempB = tempB.next
    return None

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

ha = node(1)
c = node(2)
hb = node(3)
hb.next = c
ha.next = c

print getIntersectionNode(ha, hb)
