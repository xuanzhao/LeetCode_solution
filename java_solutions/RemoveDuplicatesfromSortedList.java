public class RemoveDuplicatesfromSortedList {
	public static void main(String[] args) {
		
	}
}

class Solution {
	public ListNode deleteDuplicates(ListNode head) {
		ListNode current = head;
		while (current != null && current.next != null) {
			if (current.next.val == current.val) {
				current.next = current.next.next;
			} else {
				current = current.next;
			}
		}
		return head;		
	}
}

