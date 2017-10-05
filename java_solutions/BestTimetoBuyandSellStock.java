public class BestTimetoBuyandSellStock {
	public static void main(String[] args) {
		
	}
}


public class Solution1 {
	public int maxProfit(int[] prices) {
		int maxprofit = 0;
		for (int i = 0; i < prices.length - 1; i++) {
			for (int j = i + 1; j < prices.length; j++) {
				int profit = prices[j] - prices[i];
				if (profit > maxprofit)
					maxprofit = profit;
			}
		}
		return maxprofit;
	}
}

public class Solution2 {
	public int maxProfit(int[] prices) {
		int minprice = Integer.MAX_VALUE;
		int maxprofit = 0;
		for (int i = 0; i < prices.length; i++) {
			if (prices[i] < minprice)
				minprice = prices[i];
			else if (prices[i] - minprice > maxprofit)
				maxprofilt = prices[i] - minprice;
		}
		return maxprofit;
	}
}