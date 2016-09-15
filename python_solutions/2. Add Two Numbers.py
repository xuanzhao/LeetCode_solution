# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

	carry = 0
	head = ListNode(0)
	dummy = head
	
	while(l1 or l2):
		x = l1.val if l1 else 0
		y = l2.val if l2 else 0
		acc = x + y + carry
		head.next = ListNode( acc % 10)
		carry = acc / 10
	
		l1 = l1.next if l1 else l1
		l2 = l2.next if l2 else l2
		head = head.next
	
	if carry > 0:
		head.next = ListNode(carry)
	
	return dummy.next


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
	carry = 0
	head = ListNode(0)
	dummy = head
	
	while(l1 and l2):
		val = l1.val + l2.val + carry
		head.next = ListNode( val % 10)
		carry = val / 10
	
		l1 = l1.next
		l2 = l2.next
		head = head.next
	
	while l1:
		val = l1.val + carry
		head.next = ListNode(val %10)
		carry = val / 10
	
		l1 = l1.next
		head = head.next
	
	while l2:
		val = l2.val + carry
		head.next = ListNode(val % 10)
		carry = val /10
	
		l2 = l2.next
		head = head.next
	
	if carry > 0:
		head.next = ListNode(carry)
	
	return dummy.next
    