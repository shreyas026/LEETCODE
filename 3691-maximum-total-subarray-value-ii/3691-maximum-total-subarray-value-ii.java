// =======================================
// 3691. Maximum Total Subarray Value II
// =======================================
// Difficulty: Hard
//
// You are given an integer array `nums` of length `n` and an integer `k`.
//
// You must select **exactly** `k` **distinct** subarrays `nums[l..r]` of `nums`. Subarrays may overlap, but the exact same subarray (same `l` and `r`) **cannot** be chosen more than once.
//
// The **value** of a subarray `nums[l..r]` is defined as: `max(nums[l..r]) - min(nums[l..r])`.
//
// The **total value** is the sum of the **values** of all chosen subarrays.
//
// Return the **maximum** possible total value you can achieve.
//
//  
//
// **Example 1:**
//
// **Input:** nums = [1,3,2], k = 2
//
// **Output:** 4
//
// **Explanation:**
//
// One optimal approach is:
//
// 	
// - Choose `nums[0..1] = [1, 3]`. The maximum is 3 and the minimum is 1, giving a value of `3 - 1 = 2`.
// 	
// - Choose `nums[0..2] = [1, 3, 2]`. The maximum is still 3 and the minimum is still 1, so the value is also `3 - 1 = 2`.
//
// Adding these gives `2 + 2 = 4`.
//
// **Example 2:**
//
// **Input:** nums = [4,2,5,1], k = 3
//
// **Output:** 12
//
// **Explanation:**
//
// One optimal approach is:
//
// 	
// - Choose `nums[0..3] = [4, 2, 5, 1]`. The maximum is 5 and the minimum is 1, giving a value of `5 - 1 = 4`.
// 	
// - Choose `nums[1..3] = [2, 5, 1]`. The maximum is 5 and the minimum is 1, so the value is also `4`.
// 	
// - Choose `nums[2..3] = [5, 1]`. The maximum is 5 and the minimum is 1, so the value is again `4`.
//
// Adding these gives `4 + 4 + 4 = 12`.
//
//  
//
// **Constraints:**
//
// 	
// - `1 &lt;= n == nums.length &lt;= 5 * 10^​​​​​​​4`
// 	
// - `0 &lt;= nums[i] &lt;= 10^9`
// 	
// - `1 &lt;= k &lt;= min(10^5, n * (n + 1) / 2)`
//
// ====== SOLUTION ======

import java.util.PriorityQueue;

class Solution {
    public long maxTotalValue(int[] nums, int k) {
        int n = nums.length;
        int maxLog = 0;
        while ((1 << maxLog) <= n) {
            maxLog++;
        }

        int[][] stMax = new int[maxLog][n];
        int[][] stMin = new int[maxLog][n];

        for (int i = 0; i < n; i++) {
            stMax[0][i] = nums[i];
            stMin[0][i] = nums[i];
        }

        for (int j = 1; j < maxLog; j++) {
            for (int i = 0; i + (1 << j) <= n; i++) {
                stMax[j][i] = Math.max(stMax[j - 1][i], stMax[j - 1][i + (1 << (j - 1))]);
                stMin[j][i] = Math.min(stMin[j - 1][i], stMin[j - 1][i + (1 << (j - 1))]);
            }
        }

        int[] lg = new int[n + 1];
        for (int i = 2; i <= n; i++) {
            lg[i] = lg[i >> 1] + 1;
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0]));

        for (int l = 0; l < n; l++) {
            int val = queryValue(stMax, stMin, lg, l, n - 1);
            pq.offer(new int[]{val, l, n - 1});
        }

        long totalValue = 0;

        while (k > 0 && !pq.isEmpty()) {
            int[] curr = pq.poll();
            int val = curr[0];
            int l = curr[1];
            int r = curr[2];

            totalValue += val;
            k--;

            if (r > l) {
                int nextR = r - 1;
                int nextVal = queryValue(stMax, stMin, lg, l, nextR);
                pq.offer(new int[]{nextVal, l, nextR});
            }
        }

        return totalValue;
    }

    private int queryValue(int[][] stMax, int[][] stMin, int[] lg, int l, int r) {
        int len = r - l + 1;
        int j = lg[len];
        int maxVal = Math.max(stMax[j][l], stMax[j][r - (1 << j) + 1]);
        int minVal = Math.min(stMin[j][l], stMin[j][r - (1 << j) + 1]);
        return maxVal - minVal;
    }
}
