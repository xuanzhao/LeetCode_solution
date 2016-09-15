def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    dummy = ListNode(0)
    dummy.next = head

    h = head
    length = 0
    while(h != None):
        length += 1
        h = h.next

    left = length - n
    h = dummy
    while(left > 0):
        left -= 1
        h = h.next

    h.next = h.next.next
    
    return dummy.next


 def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """

    h = head
    lis = []
    while(h != None):
        lis.append(h.val)
        h = h.next
    
    if n > len(lis): return head
    elif n == 0: return head
    elif n == len(lis): return head.next
    
    if n < 0: 
        idx = -n - 1
        lis.pop(idx)
    else:
        idx = len(lis) - n 
        lis.pop(idx)
    
    link = ListNode(lis.pop(0))
    
    def loop(lis, head):
        if lis == []: return None
        else :
            head.next= ListNode(lis.pop(0))
            loop(lis, head.next)
    
    loop(lis, link)
    
    return link