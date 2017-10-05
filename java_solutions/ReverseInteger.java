public class ReverseInteger {
	public static void main(String[] args) {
		Solution sol = new Solution();
		System.out.println(sol.reverse(2147483648));
	}
}

class Solution {
	public int reverse(int x) throws ArithmeticException{
		try {
		boolean pos;
		if (x >= 0)
		    pos = true;
		else
		    pos = false;
		
		if (!pos)
			x = -x;
		int reverse = 0;

		while (x != 0) {
			if (reverse > (Integer.MAX_VALUE ) / 10)
			    return 0;
			reverse = reverse * 10 + x % 10;
			x = x / 10;
			//System.out.println(x);
			//System.out.println(reverse);
		}
		
		System.out.println(reverse);
		if (pos == true)
			return reverse;
		else return -reverse;
		}
		catch (ArithmeticException e) {
			throw new ArithmeticException("0");
		}
	}
}
