# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
	"""
	
	hA = headA
	hB = headB

	while(hB != None):
		while(hA != None):
			if hB == hA: return hB
			else: hA = hA.next

		hB = hB.next
		hA = headA

	return None



def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
	"""
	hA = headA
	hB = headB
	dic = {}

	while(hA != None):
		dic[hA] = id(hA)
		hA = hA.next

	while(hB != None):
		if dic.has_key(hB): return hB
		hB = hB.next

	return None


def getIntersectionNode(headA, headB):
	"""
	 :type head1, head1: ListNode
	 :rtype: ListNode
	"""
	hA = headA
	hB = headB
	
	if hA == None or hB == None: return None
	
	while(hA.next != None and hB.next != None):
		if hA == hB: return hA
		hA = hA.next
		hB = hB.next

	if hA.next == None and hB.next == None:
		hA.next = headB
		hAO = hA
		hB.next = headA
		hBO = hB
		while(hA != None and hB != None):
			hA = hA.next
			hB = hB.next
			if hA == hB: return hA

		hAO.next = None
		hBO.next = None
		return None 

	elif hA.next == None:
		hA.next = headB
		hAO = hA
		while(hB.next != None):
			if hA == hB: return hA
			hA = hA.next
			hB = hB.next
		hB.next = headA
		hBO = hB
		while(hA != None):
			if hA == hB: return hA
			hA = hA.next
			hB = hB.next

		hAO.next = None
		hBO.next = None
		return None

	elif hB.next == None:
		hB.next = headA
		hBO = hB
		while(hA.next != None):
			if hA == hB: return hA
			hA = hA.next
			hB = hB.next
		hA.next = headB
		hAO = hA
		while(hB != None):
			if hA == hB: return hA
			hA = hA.next
			hB = hB.next

		hAO.next = None
		hBO.next = None
		return None


a = ListNode(1)
a.next = ListNode(3)
a.next.next = ListNode(5)
b = ListNode(2)
b.next = a.next.next

# get a infinite circle


def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
	"""
	hA = headA
	hB = headB

	if hA == None or hB == None: return None


	while(hA != None and hB != None):
		if hA == hB: return hA
		hA = hA.next
		hB = hB.next

	if hA == None and hB == None: return None
	elif hA == None:
		hA = headB
		while(hB != None):
			if hA == hB: return hA
			hA = hA.next
			hB = hB.next

		hB = headA
		while(hA != None):
			if hA == hB: return hA
			hA = hA.next
			hB = hB.next

		return None

	else:
		hB = headA
		while(hA != None):
			if hA == hB: return hA
			hA = hA.next
			hB = hB.next

		hA = headB
		while(hB != None):
			if hA == hB: return hA
			hA = hA.next
			hB = hB.next

		return None
























