import java.util.*;

public class Solution {
	/**
	 * @param A, B: Two string.
	 * @return: the length of the longest common substring.
	 */
	public int longestCommonSubstring(String A, String B) {
		// write your code here
		if (A == null || B == null || A.length() == 0 || B.length() == 0)
			return 0;
		int lenA = A.length();
		int lenB = B.length();
		int [][] C = new int[lenA+1][lenB+1];
		int longest = 0;
		
		for (int i = 1; i <= lenA; i++) {
			for (int j = 1; j <= lenB; j++) {
				int m = i;
				int n = j;
				while (m < lenA && n < lenB) {
					char ch1 = A.charAt(m-1);
					char ch2 = B.charAt(n-1);
					if (ch1 == ch2) {
						C[m][n] = C[m-1][n-1] + 1;
						m++;
						n++;
					}
					else {
						C[m][n] = Math.max(C[m-1][n-1], 0);
						break;
					}
				}
				longest = Math.max(longest, C[m][n]);
			}
		}
		System.out.println(longest);
		return longest;
	}
	
	public static void main(String[] args) {
		Solution lcs = new Solution();
		lcs.longestCommonSubstring("www.lintcode.com code", "www.ninechapter.com code");
	}
}