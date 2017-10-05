public class RangeSumQuery-Immutable {
	public static void main(String[] args) {
		
	}
}

public class NumArray {
	
	private Map<Pair<Integer, Integer>, Integer> map = new HashMap<>();
	
	public NumArray(int[] nums) {
		for (int i = 0; i < nums.length; i++) {
			int sum = 0;
			for (int j = i; j < nums.length; j++) {
				sum += nums[j];
				map.put(Pair.create(i,j), sum);
			}
		}	
	}

	public int sumRange(int i, int j) {
		return map.get(Pair.create(i, j));
	}
}


public class NumArray {
	private int[] sum;
	
	public NumArray(int[] nums) {
		sum = new int[nums.length + 1];
		for (int i = 0; i < nums.length; i++) {
			sum[i + 1] = sum[i] + nums[i];
		}
	}
	
	public int sumRange(int i, int j) {
		return sum[j + 1] - sum[i];
	}
}