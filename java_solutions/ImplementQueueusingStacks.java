import java.util.*;

public class ImplementQueueusingStacks {
	public static void main(String[] args) {
		
	}
	
}


class MyQueue {
	
	private Stack<Integer> s1 = new Stack<>();
	private Stack<Integer> s2 = new Stack<>();
	private int front;
	
	// Push element x to the back of queue.
	public void push(int x) {
		if (s1.isEmpty())
		    front = x;
		s1.push(x);
	}

	// Removes the element from in front of queue.
	public void pop() {
		if (s2.isEmpty()) {
			while (!s1.isEmpty()) {
				s2.push(s1.pop());
			}
		}
		s2.pop();
	}

	// Get the front element.
	public int peek() {
		if (!s2.isEmpty()) {
			return s2.peek();
		}
		return front;
	}

	// Return whether the queue is empty.
	public boolean empty() {
		return s1.isEmpty() && s2.isEmpty();
	}
}