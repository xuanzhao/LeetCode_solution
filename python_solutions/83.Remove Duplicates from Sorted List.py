# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
    	dummy = ListNode(None)
    	prev = dummy
    	prev.next = head
    	h = head
    	
    	if h == None: return 
    	
    	while(h != None):
    		car = h
    		cdr = h.next
    		
    		if cdr != None and cdr.val == car.val:
    			while(cdr != None and cdr.val == car.val and cdr != None):
    				cdr = cdr.next
    
    			h.next = cdr
    			prev = h
    			h = h.next
    		
    		else:
    			prev = h
    			h = cdr
    			
        return dummy.next

def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
        dummy = ListNode(None)
        dummy.next = head
        h = head
        
        if h == None: return 
        
        while(h != None):
            car = h
            cdr = h.next
            
            if cdr != None and cdr.val == car.val:
                while(cdr != None and cdr.val == car.val and cdr != None):
                    cdr = cdr.next
    
                h.next = cdr
                h = h.next
            
            else:
                h = cdr
                
        return dummy.next

        
def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    current = head
    
    while(current != None and current.next != None):
        if (current.next.val == current.val):
            current.next = current.next.next
        else:
            current = current.next
            
    return head