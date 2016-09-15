# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
	"""
	:type head: ListNode
	:rtype: bool
	"""
	
	
	def loop(head, current):
		
		if current == None: return False
		else:
			if current.next == current: return True
			next = head
			while(next != current):
				if current.next == next: return True
				next = next.next
	
	
			current = current.next
			return loop(head, current)
	
	return loop(head,head)



a = ListNode(3)
a.next = ListNode(2)
a.next.next = ListNode(0)
a.next.next.next = ListNode(-4)
a.next.next.next.next = a.next
			


def hasCycle(head):
	"""
	:type head: ListNode
	:rtype: bool
	"""
	h = head
	dic = {}
	while(h != None):
		if dic.has_key(h): return True
		else: 
			dic[h] = id(h)
			h = h.next
	return False



def hasCycle(head):
	"""
	:type head: ListNode
	:rtype: bool
	"""
	
	if (head == None or head.next == None): return False
	
	fast = head.next
	slow = head
	while(slow != fast):
		if (fast == None or fast.next == None): return False
		slow = slow.next
		fast = fast.next.next
	
	return True




















