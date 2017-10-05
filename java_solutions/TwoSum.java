import java.util.HashMap;
import java.util.Arrays;

public class TwoSum {
	public static void main(String[] args) {
		Solution1 sol1 = new Solution1();
		Solution2 sol2 = new Solution2();
		
		int[] nums = {2, 7, 11, 15};
		int target = 9;
		int[] result;
		
		result = sol1.twoSum(nums, target);
		System.out.println(Arrays.toString(result));
		
		result = sol2.twoSum(nums, target);
		System.out.println(Arrays.toString(result));
		
	}
}

class Solution1 {
	public int[] twoSum(int[] nums, int target) {
		HashMap<Integer, Integer> m = new HashMap<Integer, Integer>();
		int[] res = new int[2];
		for (int i = 0; i < nums.length; ++i) {
			m.put(nums[i], i);
		}
		for (int i = 0; i < nums.length; ++i) {
			int t = target - nums[i];
			if (m.containsKey(t) && m.get(t) != i) {
				res[0] = i;
				res[1] = m.get(t);
				break;
			}
		}
		return res;
	}
}


class Solution2 {
	public int[] twoSum(int[] nums, int target) {
		HashMap<Integer,Integer> map = new HashMap<>();
		
		for (int i = 0; i < nums.length; i++) {
			int complement = target - nums[i];
			if (map.containsKey(complement)) {
				return new int[] { map.get(complement), i};
			}
			map.put(nums[i], i);
		}
		throw new IllegalArgumentException("No two sum solution");
	}
}