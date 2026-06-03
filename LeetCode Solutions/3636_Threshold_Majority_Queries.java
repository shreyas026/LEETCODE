// ==================================
// 3636. Threshold Majority Queries
// ==================================
// Difficulty: Hard
//
// You are given an integer array `nums` of length `n` and an array `queries`, where `queries[i] = [l_i, r_i, threshold_i]`.
//
// Return an array of integers `ans` where `ans[i]` is equal to the element in the subarray `nums[l_i...r_i]` that appears **at least** `threshold_i` times, selecting the element with the **highest** frequency (choosing the **smallest** in case of a tie), or -1 if no such element *exists*.
//
//  
//
// **Example 1:**
//
// **Input:** nums = [1,1,2,2,1,1], queries = [[0,5,4],[0,3,3],[2,3,2]]
//
// **Output:** [1,-1,2]
//
// **Explanation:**
//
// 	
// 		
// 			Query
// 			Sub-array
// 			Threshold
// 			Frequency table
// 			Answer
// 		
// 	
// 	
// 		
// 			[0, 5, 4]
// 			[1, 1, 2, 2, 1, 1]
// 			4
// 			1 &rarr; 4, 2 &rarr; 2
// 			1
// 		
// 		
// 			[0, 3, 3]
// 			[1, 1, 2, 2]
// 			3
// 			1 &rarr; 2, 2 &rarr; 2
// 			-1
// 		
// 		
// 			[2, 3, 2]
// 			[2, 2]
// 			2
// 			2 &rarr; 2
// 			2
// 		
// 	
//
// **Example 2:**
//
// **Input:** nums = [3,2,3,2,3,2,3], queries = [[0,6,4],[1,5,2],[2,4,1],[3,3,1]]
//
// **Output:** [3,2,3,2]
//
// **Explanation:**
//
// 	
// 		
// 			Query
// 			Sub-array
// 			Threshold
// 			Frequency table
// 			Answer
// 		
// 	
// 	
// 		
// 			[0, 6, 4]
// 			[3, 2, 3, 2, 3, 2, 3]
// 			4
// 			3 &rarr; 4, 2 &rarr; 3
// 			3
// 		
// 		
// 			[1, 5, 2]
// 			[2, 3, 2, 3, 2]
// 			2
// 			2 &rarr; 3, 3 &rarr; 2
// 			2
// 		
// 		
// 			[2, 4, 1]
// 			[3, 2, 3]
// 			1
// 			3 &rarr; 2, 2 &rarr; 1
// 			3
// 		
// 		
// 			[3, 3, 1]
// 			[2]
// 			1
// 			2 &rarr; 1
// 			2
// 		
// 	
//
//  
//
// **Constraints:**
//
// 	
// - `1 &lt;= nums.length == n &lt;= 10^4`
// 	
// - `1 &lt;= nums[i] &lt;= 10^9`
// 	
// - `1 &lt;= queries.length &lt;= 5 * 10^4`
// 	
// - `queries[i] = [l_i, r_i, threshold_i]`
// 	
// - `0 &lt;= l_i &lt;= r_i &lt; n`
// 	
// - `1 &lt;= threshold_i &lt;= r_i - l_i + 1`
//
// ====== SOLUTION ======

import java.util.*;

class Solution {

    static class Query {
        int l, r, threshold, idx;

        Query(int l, int r, int threshold, int idx) {
            this.l = l;
            this.r = r;
            this.threshold = threshold;
            this.idx = idx;
        }
    }

    public int[] subarrayMajority(int[] nums, int[][] queries) {

        int n = nums.length;
        int q = queries.length;

        TreeSet<Integer> values = new TreeSet<>();
        for (int x : nums) values.add(x);

        Map<Integer, Integer> compress = new HashMap<>();
        ArrayList<Integer> actual = new ArrayList<>();

        int id = 0;
        for (int v : values) {
            compress.put(v, id++);
            actual.add(v);
        }

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = compress.get(nums[i]);
        }

        Query[] qs = new Query[q];
        for (int i = 0; i < q; i++) {
            qs[i] = new Query(
                queries[i][0],
                queries[i][1],
                queries[i][2],
                i
            );
        }

        int block = (int) Math.sqrt(n);

        Arrays.sort(qs, (a, b) -> {
            int ba = a.l / block;
            int bb = b.l / block;

            if (ba != bb) return ba - bb;

            if ((ba & 1) == 0) {
                return a.r - b.r;
            }
            return b.r - a.r;
        });

        int m = id;

        int[] freq = new int[m];

        @SuppressWarnings("unchecked")
        TreeSet<Integer>[] bucket = new TreeSet[n + 2];

        Comparator<Integer> cmp =
            (x, y) -> {
                int vx = actual.get(x);
                int vy = actual.get(y);
                if (vx != vy) return Integer.compare(vx, vy);
                return Integer.compare(x, y);
            };

        for (int i = 0; i <= n + 1; i++) {
            bucket[i] = new TreeSet<>(cmp);
        }

        int maxFreq = 0;

        int curL = 0;
        int curR = -1;

        int[] ans = new int[q];

        for (Query qu : qs) {

            while (curL > qu.l) {
                curL--;
                int v = arr[curL];

                int f = freq[v];
                if (f > 0) bucket[f].remove(v);

                freq[v]++;

                bucket[f + 1].add(v);
                maxFreq = Math.max(maxFreq, f + 1);
            }

            while (curR < qu.r) {
                curR++;
                int v = arr[curR];

                int f = freq[v];
                if (f > 0) bucket[f].remove(v);

                freq[v]++;

                bucket[f + 1].add(v);
                maxFreq = Math.max(maxFreq, f + 1);
            }

            while (curL < qu.l) {
                int v = arr[curL];

                int f = freq[v];
                bucket[f].remove(v);

                freq[v]--;

                if (f - 1 > 0) {
                    bucket[f - 1].add(v);
                }

                curL++;
            }

            while (curR > qu.r) {
                int v = arr[curR];

                int f = freq[v];
                bucket[f].remove(v);

                freq[v]--;

                if (f - 1 > 0) {
                    bucket[f - 1].add(v);
                }

                curR--;
            }

            while (maxFreq > 0 && bucket[maxFreq].isEmpty()) {
                maxFreq--;
            }

            if (maxFreq < qu.threshold) {
                ans[qu.idx] = -1;
            } else {
                int bestId = bucket[maxFreq].first();
                ans[qu.idx] = actual.get(bestId);
            }
        }

        return ans;
    }
}
