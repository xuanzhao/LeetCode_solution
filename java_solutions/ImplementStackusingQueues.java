import java.util.*;

public class ImplementStackusingQueues {
	public static void main(String[] args) {
		
	}
}

class MyStack {
	
	private Queue<Integer> q1 = new LinkedList<>();
	private Queue<Integer> q2 = new LinkedList<>();
	private int top;

	// Push element x onto stack.
	public void push(int x) {
		q1.add(x);
		top = x;
	}

	// Removes the element on top of the stack.
	public void pop() {
		while (q1.size() > 1) {
			top = q1.remove();
			q2.add(top);
		}
		q1.remove();
		Queue<Integer> temp = q1;
		q1 = q2;
		q2 = temp;
		
	}

	// Get the top element.
	public int top() {
		return top;
	}

	// Return whether the stack is empty.
	public boolean empty() {
		return q1.isEmpty();
	}
}