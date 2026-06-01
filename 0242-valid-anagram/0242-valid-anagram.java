// ====================
// 242. Valid Anagram
// ====================
// Difficulty: Easy
//
// Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.
//
//  
//
// **Example 1:**
//
// **Input:** s = &quot;anagram&quot;, t = &quot;nagaram&quot;
//
// **Output:** true
//
// **Example 2:**
//
// **Input:** s = &quot;rat&quot;, t = &quot;car&quot;
//
// **Output:** false
//
//  
//
// **Constraints:**
//
// 	
// - `1 &lt;= s.length, t.length &lt;= 5 * 10^4`
// 	
// - `s` and `t` consist of lowercase English letters.
//
//  
//
// **Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
//
// ====== SOLUTION ======

class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()) return false;

        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();

        Arrays.sort(sChars);
        Arrays.sort(tChars);

        return Arrays.equals(sChars, tChars);
    }
}
