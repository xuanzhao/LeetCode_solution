import java.util.*;

public class IntersectionofTwoLinkedLists {
	public static void main(String[] args) {
		
	}
}


public class Solution1 {
	public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
		Set<ListNode> nodeSeen = new HashSet<>();
		while (headA != null) {
			if (nodeSeen.contains(headA))
				headA = headA.next;
			else {
				nodeSeen.add(headA);
				headA = headA.next;
			}
		}
		while (headB != null) {
			if (nodeSeen.contains(headB))
				return headB;
			else 
				headB = headB.next;
		}
		return null;
	}
}

