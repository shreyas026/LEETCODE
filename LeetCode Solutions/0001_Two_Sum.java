// ============
// 1. Two Sum
// ============
// Difficulty: Easy
//
// You are given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.
//
// You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.
//
// You can return the answer in any order.
//
//  
//
// **Example 1:**
//
// **Input:** nums = [2,7,11,15], target = 9
// **Output:** [0,1]
// **Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].
//
// ```
//
// **Example 2:**
//
// **Input:** nums = [3,2,4], target = 6
// **Output:** [1,2]
//
// ```
//
// **Example 3:**
//
// **Input:** nums = [3,3], target = 6
// **Output:** [0,1]
//
// ```
//
//  
//
// **Constraints:**
//
// 	
// - `2 &lt;= nums.length &lt;= 10^4`
// 	
// - `-10^9 &lt;= nums[i] &lt;= 10^9`
// 	
// - `-10^9 &lt;= target &lt;= 10^9`
// 	
// - **Only one valid answer exists.**
//
//  
//
// **Follow-up: **Can you come up with an algorithm that is less than `O(n^2)`` `time complexity?
//
// ====== SOLUTION ======

public class Solution {
    public static int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] {i, j};
                }
            }
        }
        return new int[] {}; 
    }

    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        
        int[] result = twoSum(nums, target);
        System.out.println("[" + result[0] + ", " + result[1] + "]");
    }
}
