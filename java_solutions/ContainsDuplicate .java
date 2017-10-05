public class ContainsDuplicate {
	public static void main(String[] args) {
		
	}
}


public class Solution1 {
	public boolean containsDuplicate(int[] nums) {
		for (int i = 0; i < nums.length; i++) {
			for (int j = i+1; j < nums.length; j++) {
				if (nums[j] == nums[i]) return true;
			}
		}
		return false;
	}
}

public class Solution2 {
	public boolean containsDuplicate(int[] nums) {
		Arrays.sort(nums);
		for (int i = 0; i < nums.length - 1; i++) {
			if (nums[i] == nums[i+1])
				return true;
		}
		return false;
	}
}

public class Solution3 {
	Set<Integer> set = new HashSet<>(nums.length);
	for (int x: nums) {
		if (set.contains(x)) return true;
		set.add(x);
	}
	return false;
}
