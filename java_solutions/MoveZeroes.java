public class MoveZeroes {
	public static void main(String[] args) {
		
	}
}

public class Solution1 {
	public void moveZeroes(int[] nums) {
		int count = 0;
		for (int i = 0; i < nums.length; i++) {
			if (nums[i] != 0) {
				nums[count] = nums[i];
				count++;
			}
		}
		for (int c = count; c < nums.length; c++) {
			nums[m] = 0;
		}
		
	}
}
