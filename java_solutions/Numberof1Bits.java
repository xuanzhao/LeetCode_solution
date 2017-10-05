class Numberof1Bits {
	public static void main(String[] args) {
		
	}
}


public class Solution1 {
	// you need to treat n as an unsigned value
	public int hammingWeight(int n) {
		int bits = 0;
		int mask = 1;
		for (int i = 0; i < 32; i++) {
			if ((n & mask) != 0) {
				bits++;
			}
			mask <<= 1;
		}
		return bits;
	}
}

public class Solution2 {
	public int hammingWeight(int n) {
		int sum = 0;
		while (n != 0) {
			sum++;
			n &= (n - 1);
		}
		return sum;
	}
}
	