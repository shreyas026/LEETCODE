// ========================================================
// 3635. Earliest Finish Time for Land and Water Rides II
// ========================================================
// Difficulty: Medium
//
// You are given two categories of theme park attractions: **land rides** and **water rides**.
//
// 	
// - **Land rides**
//
// 	
//
// 		
// - `landStartTime[i]` &ndash; the earliest time the `i^th` land ride can be boarded.
// 		
// - `landDuration[i]` &ndash; how long the `i^th` land ride lasts.
// 	
//
// 	
// 	
// - **Water rides**
// 	
//
// 		
// - `waterStartTime[j]` &ndash; the earliest time the `j^th` water ride can be boarded.
// 		
// - `waterDuration[j]` &ndash; how long the `j^th` water ride lasts.
// 	
//
// 	
//
// A tourist must experience **exactly one** ride from **each** category, in **either order**.
//
// 	
// - A ride may be started at its opening time or **any later moment**.
// 	
// - If a ride is started at time `t`, it finishes at time `t + duration`.
// 	
// - Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.
//
// Return the **earliest possible time** at which the tourist can finish both rides.
//
//  
//
// **Example 1:**
//
// **Input:** landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]
//
// **Output:** 9
//
// **Explanation:**​​​​​​​
//
// 	
// - Plan A (land ride 0 &rarr; water ride 0):
// 	
//
// 		
// - Start land ride 0 at time `landStartTime[0] = 2`. Finish at `2 + landDuration[0] = 6`.
// 		
// - Water ride 0 opens at time `waterStartTime[0] = 6`. Start immediately at `6`, finish at `6 + waterDuration[0] = 9`.
// 	
//
// 	
// 	
// - Plan B (water ride 0 &rarr; land ride 1):
// 	
//
// 		
// - Start water ride 0 at time `waterStartTime[0] = 6`. Finish at `6 + waterDuration[0] = 9`.
// 		
// - Land ride 1 opens at `landStartTime[1] = 8`. Start at time `9`, finish at `9 + landDuration[1] = 10`.
// 	
//
// 	
// 	
// - Plan C (land ride 1 &rarr; water ride 0):
// 	
//
// 		
// - Start land ride 1 at time `landStartTime[1] = 8`. Finish at `8 + landDuration[1] = 9`.
// 		
// - Water ride 0 opened at `waterStartTime[0] = 6`. Start at time `9`, finish at `9 + waterDuration[0] = 12`.
// 	
//
// 	
// 	
// - Plan D (water ride 0 &rarr; land ride 0):
// 	
//
// 		
// - Start water ride 0 at time `waterStartTime[0] = 6`. Finish at `6 + waterDuration[0] = 9`.
// 		
// - Land ride 0 opened at `landStartTime[0] = 2`. Start at time `9`, finish at `9 + landDuration[0] = 13`.
// 	
//
// 	
//
// Plan A gives the earliest finish time of 9.
//
// **Example 2:**
//
// **Input:** landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]
//
// **Output:** 14
//
// **Explanation:**​​​​​​​
//
// 	
// - Plan A (water ride 0 &rarr; land ride 0):
// 	
//
// 		
// - Start water ride 0 at time `waterStartTime[0] = 1`. Finish at `1 + waterDuration[0] = 11`.
// 		
// - Land ride 0 opened at `landStartTime[0] = 5`. Start immediately at `11` and finish at `11 + landDuration[0] = 14`.
// 	
//
// 	
// 	
// - Plan B (land ride 0 &rarr; water ride 0):
// 	
//
// 		
// - Start land ride 0 at time `landStartTime[0] = 5`. Finish at `5 + landDuration[0] = 8`.
// 		
// - Water ride 0 opened at `waterStartTime[0] = 1`. Start immediately at `8` and finish at `8 + waterDuration[0] = 18`.
// 	
//
// 	
//
// Plan A provides the earliest finish time of 14.**​​​​​​​**
//
//  
//
// **Constraints:**
//
// 	
// - `1 &lt;= n, m &lt;= 5 * 10^4`
// 	
// - `landStartTime.length == landDuration.length == n`
// 	
// - `waterStartTime.length == waterDuration.length == m`
// 	
// - `1 &lt;= landStartTime[i], landDuration[i], waterStartTime[j], waterDuration[j] &lt;= 10^5`
//
// ====== SOLUTION ======

import java.util.Arrays;

class Solution {

    private int upperBound(int[] arr, int target) {
        int left = 0, right = arr.length;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (arr[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }

    private int solve(int[] startA, int[] durA,
                      int[] startB, int[] durB) {

        int n = startB.length;

        int[][] rides = new int[n][2];
        for (int i = 0; i < n; i++) {
            rides[i][0] = startB[i];
            rides[i][1] = durB[i];
        }

        Arrays.sort(rides, (a, b) -> Integer.compare(a[0], b[0]));

        int[] starts = new int[n];
        int[] prefMinDur = new int[n];
        int[] suffMinSum = new int[n];

        starts[0] = rides[0][0];
        prefMinDur[0] = rides[0][1];

        for (int i = 1; i < n; i++) {
            starts[i] = rides[i][0];
            prefMinDur[i] = Math.min(prefMinDur[i - 1], rides[i][1]);
        }

        suffMinSum[n - 1] = rides[n - 1][0] + rides[n - 1][1];

        for (int i = n - 2; i >= 0; i--) {
            suffMinSum[i] = Math.min(
                suffMinSum[i + 1],
                rides[i][0] + rides[i][1]
            );
        }

        int ans = Integer.MAX_VALUE;

        for (int i = 0; i < startA.length; i++) {
            int finishTime = startA[i] + durA[i];

            int pos = upperBound(starts, finishTime);

            if (pos > 0) {
                ans = Math.min(
                    ans,
                    finishTime + prefMinDur[pos - 1]
                );
            }

            if (pos < n) {
                ans = Math.min(
                    ans,
                    suffMinSum[pos]
                );
            }
        }

        return ans;
    }

    public int earliestFinishTime(int[] landStartTime,
                                  int[] landDuration,
                                  int[] waterStartTime,
                                  int[] waterDuration) {

        return Math.min(
            solve(
                landStartTime,
                landDuration,
                waterStartTime,
                waterDuration
            ),
            solve(
                waterStartTime,
                waterDuration,
                landStartTime,
                landDuration
            )
        );
    }
}
