/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

//Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
//Output: 7 -> 0 -> 8

public class AddTwoNumbers {
	public static void main(String[] args) {
		
	}	
}

class Solution {
	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		int carry = 0;
		ListNode head = new ListNode(0);
		ListNode dummy = head;
		int x, y, acc;
		
		while (l1 != null || l2 != null) {
			x = l1 == null ? 0 : l1.val;
			y = l2 == null ? 0 : l2.val;
			
			acc = x + y + carry;
			head.next = new ListNode(acc % 10);
			carry = acc / 10;
			
			if (l1 != null) l1 = l1.next;
			if (l2 != null) l2 = l2.next;
			head = head.next;
		}
		
		if (carry > 0) head.next = new ListNode(carry);
		
		return dummy.next;
	}
}
