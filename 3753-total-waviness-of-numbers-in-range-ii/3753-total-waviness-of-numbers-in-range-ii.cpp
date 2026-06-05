// =============================================
// 3753. Total Waviness of Numbers in Range II
// =============================================
// Difficulty: Hard
//
// You are given two integers `num1` and `num2` representing an **inclusive** range `[num1, num2]`.
//
// The **waviness** of a number is defined as the total count of its **peaks** and **valleys**:
//
// 	
// - A digit is a **peak** if it is **strictly greater** than both of its immediate neighbors.
// 	
// - A digit is a **valley** if it is **strictly less** than both of its immediate neighbors.
// 	
// - The first and last digits of a number **cannot** be peaks or valleys.
// 	
// - Any number with fewer than 3 digits has a waviness of 0.
//
// Return the total sum of waviness for all numbers in the range `[num1, num2]`.
//
//  
//
// **Example 1:**
//
// **Input:** num1 = 120, num2 = 130
//
// **Output:** 3
//
// **Explanation:**
//
// In the range `[120, 130]`:
//
// 	
// - `120`: middle digit 2 is a peak, waviness = 1.
// 	
// - `121`: middle digit 2 is a peak, waviness = 1.
// 	
// - `130`: middle digit 3 is a peak, waviness = 1.
// 	
// - All other numbers in the range have a waviness of 0.
//
// Thus, total waviness is `1 + 1 + 1 = 3`.
//
// **Example 2:**
//
// **Input:** num1 = 198, num2 = 202
//
// **Output:** 3
//
// **Explanation:**
//
// In the range `[198, 202]`:
//
// 	
// - `198`: middle digit 9 is a peak, waviness = 1.
// 	
// - `201`: middle digit 0 is a valley, waviness = 1.
// 	
// - `202`: middle digit 0 is a valley, waviness = 1.
// 	
// - All other numbers in the range have a waviness of 0.
//
// Thus, total waviness is `1 + 1 + 1 = 3`.
//
// **Example 3:**
//
// **Input:** num1 = 4848, num2 = 4848
//
// **Output:** 2
//
// **Explanation:**
//
// Number `4848`: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.
//
//  
//
// **Constraints:**
//
// 	
// - `1 &lt;= num1 &lt;= num2 &lt;= 10^15`​​​​​​​
//
// ====== SOLUTION ======

class Solution {
public:
    struct Node {
        long long cnt;
        long long sum;
    };

    string s;
    Node memo[20][11][11][2];
    bool vis[20][11][11][2];

    Node dfs(int pos, int prev1, int prev2,
             bool started, bool tight) {
        if (pos == (int)s.size()) {
            return {1, 0};
        }

        if (!tight && started &&
            vis[pos][prev1 + 1][prev2 + 1][1]) {
            return memo[pos][prev1 + 1][prev2 + 1][1];
        }

        if (!tight && !started &&
            vis[pos][10][10][0]) {
            return memo[pos][10][10][0];
        }

        int up = tight ? (s[pos] - '0') : 9;

        long long totalCnt = 0;
        long long totalSum = 0;

        for (int d = 0; d <= up; d++) {
            bool nTight = tight && (d == up);

            if (!started && d == 0) {
                Node nxt = dfs(pos + 1, -1, -1, false, nTight);
                totalCnt += nxt.cnt;
                totalSum += nxt.sum;
                continue;
            }

            if (!started) {
                Node nxt = dfs(pos + 1, d, -1, true, nTight);
                totalCnt += nxt.cnt;
                totalSum += nxt.sum;
                continue;
            }

            long long add = 0;

            if (prev2 != -1) {
                if ((prev1 > prev2 && prev1 > d) ||
                    (prev1 < prev2 && prev1 < d)) {
                    add = 1;
                }
            }

            Node nxt = dfs(pos + 1, d, prev1, true, nTight);

            totalCnt += nxt.cnt;
            totalSum += nxt.sum + add * nxt.cnt;
        }

        Node res{totalCnt, totalSum};

        if (!tight) {
            if (started) {
                vis[pos][prev1 + 1][prev2 + 1][1] = true;
                memo[pos][prev1 + 1][prev2 + 1][1] = res;
            } else {
                vis[pos][10][10][0] = true;
                memo[pos][10][10][0] = res;
            }
        }

        return res;
    }

    long long solve(long long x) {
        if (x < 0) return 0;

        s = to_string(x);
        memset(vis, 0, sizeof(vis));

        return dfs(0, -1, -1, false, true).sum;
    }

    long long totalWaviness(long long num1, long long num2) {
        auto melidroni = make_pair(num1, num2);
        return solve(num2) - solve(num1 - 1);
    }
};
