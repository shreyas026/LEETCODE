// ===========================
// 14. Longest Common Prefix
// ===========================
// Difficulty: Easy
//
// Write a function to find the longest common prefix string amongst an array of strings.
//
// If there is no common prefix, return an empty string `&quot;&quot;`.
//
//  
//
// **Example 1:**
//
// **Input:** strs = [&quot;flower&quot;,&quot;flow&quot;,&quot;flight&quot;]
// **Output:** &quot;fl&quot;
//
// ```
//
// **Example 2:**
//
// **Input:** strs = [&quot;dog&quot;,&quot;racecar&quot;,&quot;car&quot;]
// **Output:** &quot;&quot;
// **Explanation:** There is no common prefix among the input strings.
//
// ```
//
//  
//
// **Constraints:**
//
// 	
// - `1 &lt;= strs.length &lt;= 200`
// 	
// - `0 &lt;= strs[i].length &lt;= 200`
// 	
// - `strs[i]` consists of only lowercase English letters if it is non-empty.
//
// ====== SOLUTION ======

class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length == 0 || strs == null) return "";
        String pre = strs[0];

        for(int i=1;i<strs.length;i++){
            while(strs[i].indexOf(pre)!=0){
                pre = pre.substring(0, pre.length()-1);
                if(pre.isEmpty()){
                        return "";
                 }
            }
        }
        return pre;

    } 
}
