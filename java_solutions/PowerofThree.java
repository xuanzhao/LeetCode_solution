public class PowerofThree {
	public static void main(String[] args) {
		
	}
}


class Solution1 {
	public boolean isPowerOfThree(int n) {
		if (n < 1) return false;
		
		while (n % 3 == 0) {
			n /= 3;
		}
		
		return n == 1;
	}
}

class Solution2 {
	public boolean isPowerOfThree(int n) {
		return (Math.log10(n) / Math.log10(3)) % 1 == 0;
	}
}
