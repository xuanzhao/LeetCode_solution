import java.util.*;

public class ContainsDuplicateII {
	public static void main(String[] args) {
		
	}
}


public class Solution1 {
	public boolean containsNearbyDuplicate(int[] nums, int k) {
		HashMap<Integer,Integer> map = new HashMap<>();
		int min = Integer.MAX_VALUE;
		
		for (int i = 0; i < nums.length; i++) {
			if (map.containsKey(nums[i])) {
				int preIndex = map.get(nums[i]);
				int gap = i-preIndex;
				min = Math.min(min,gap);
			}
			map.put(nums[i], i);
		}
		
		if (min <= k) {
			return true;
		} else {
			return false;
		}
	}
}

public class Solution2 {
	public boolean containsNearbyDuplicate(int[] nums, int k) {
		HashMap<Integer, Integer> map = new HashMap<>();
		
		for (int i = 0; i < nums.length; i++) {
			if (map.containsKey(nums[i])) {
				int pre = map.get(nums[i]);
				if (i-pre <= k)
					return true;
			}
			map.put(nums[i], i);
		}
		return false;
	}
}


public class Solution3 {
	public boolean ContainsNearbyDuplicate(int[] nums, int k) {
		HashMap<Integer,Integer> map = new HashMap<>();
		for (int i = 0; i < nums.length; i++) {
			if (map.containsKey(nums[i])) {
				if (Math.abs(map.get(nums[i]) - i) <= k) {
					return true;
				} else {
					map.put(nums[i], i);
				}
			} else {
				map.put(nums[i], i);
			}
		}
		return false;
	}
}
