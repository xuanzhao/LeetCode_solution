# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
	"""
	:type head: ListNode
	:rtype: ListNode
	"""
	
	car = head
	try:
		cdr = car.next
	except: cdr = None
	
	
	while(cdr != None):
		cddr = cdr.next
		car.next = None  # this is wrong
		cdr.next = car
		car = cdr
		cdr = cddr
	
	return car


def reverseList(head):
	"""
	:type head: ListNode
	:rtype: ListNode
	"""

	newHead = ListNode(-1)

	while head:
		tmp = newHead.next
		newHead.next = head
		head = head.next
		h.next = newHead 
		newHead.next.next = tmp

	return newHead.next


a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)










