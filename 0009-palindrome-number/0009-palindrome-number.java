// ======================
// 9. Palindrome Number
// ======================
// Difficulty: Easy
//
// Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.
//
//  
//
// **Example 1:**
//
// **Input:** x = 121
// **Output:** true
// **Explanation:** 121 reads as 121 from left to right and from right to left.
//
// ```
//
// **Example 2:**
//
// **Input:** x = -121
// **Output:** false
// **Explanation:** From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
//
// ```
//
// **Example 3:**
//
// **Input:** x = 10
// **Output:** false
// **Explanation:** Reads 01 from right to left. Therefore it is not a palindrome.
//
// ```
//
//  
//
// **Constraints:**
//
// 	
// - `-2^31 &lt;= x &lt;= 2^31 - 1`
//
//  
//
// **Follow up:** Could you solve it without converting the integer to a string?
//
// ====== SOLUTION ======

class Solution {
    public boolean isPalindrome(int x) {
        if(x<0) return false ;
        int on = x;
        int rn = 0;

        while(x!=0){
            int rem = x%10;
            rn = (rn*10)+rem;
            x /=10;
        }
        return on == rn;
        
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();

        Solution s = new Solution();
        System.out.println(s.isPalindrome(x));
    }
}
