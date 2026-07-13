// ===================================
// 238. Product of Array Except Self
// ===================================
// Difficulty: Medium
//
// Given an integer array `nums`, return *an array* `answer` *such that* `answer[i]` *is equal to the product of all the elements of* `nums` *except* `nums[i]`.
//
// The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.
//
// You must write an algorithm that runs in `O(n)` time and without using the division operation.
//
//  
//
// **Example 1:**
//
// **Input:** nums = [1,2,3,4]
// **Output:** [24,12,8,6]
//
// ```
//
// **Example 2:**
//
// **Input:** nums = [-1,1,0,-3,3]
// **Output:** [0,0,9,0,0]
//
// ```
//
//  
//
// **Constraints:**
//
// 	
// - `2 &lt;= nums.length &lt;= 10^5`
// 	
// - `-30 &lt;= nums[i] &lt;= 30`
// 	
// - The input is generated such that `answer[i]` is **guaranteed** to fit in a **32-bit** integer.
//
//  
//
// **Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)
//
// ====== SOLUTION ======

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] l2r = new int[nums.length];
        int[] r2l = new int[nums.length];
        int n = nums.length;
        int a=0;
        for(int i=1;i<n;i++){
            l2r[0]=1;
            l2r[i]=nums[a]*l2r[i-1];
            a+=1;
        }
        a=n-1;
        for(int i=n-2;i>=0;i--){
            r2l[n-1]=1;
            r2l[i]=nums[a]*r2l[i+1];
            a-=1;
        }
        int[] ans = new int[n];
        for(int i=0;i<n;i++){
            ans[i]=l2r[i]*r2l[i];
        }
        return ans ;
    }
}
