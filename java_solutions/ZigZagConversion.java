public class ZigZagConversion {
	public static void main(String[] args) {
		
	}
}



class Solution {
	public String convert(String s, int numRows) {
		if (numRows == 1) return s;
		
		int length = 2 * numRows - 2;
		StringBuffer res = new StringBuffer();
		
		for (int i = 0; i < numRows; i++) {
			for (int j = i; j < s.length(); j += length) {
				res.append(s.charAt(j));
				int tmp = j + length - 2 * i;
				if (i != 0 && i != numRows -1 && tmp < s.length())
				    res.append(s.charAt(tmp));
			} 
		}
		
		return res.toString();
	}
}

public class Solution {
	public String convert(String s, int numRows) {
		if (numRows <= 1) return s;
		String res = "";
		int size = 2 * numRows - 2;
		
		for (int i = 0; i < numRows; ++i) {
			for (int j = i; j < s.length(); j += size) {
				res += s.charAt(j);
				int tmp = j + size - 2 * i;
				if (i != 0 && i != numRows - 1 && tmp < s.length()) res += s.charAt(tmp);
			}
		}
		return res;
	}
}