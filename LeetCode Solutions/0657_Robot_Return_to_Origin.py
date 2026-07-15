# =============================
# 657. Robot Return to Origin
# =============================
# Difficulty: Easy
#
# There is a robot starting at the position `(0, 0)`, the origin, on a 2D plane. Given a sequence of its moves, judge if this robot **ends up at **`(0, 0)` after it completes its moves.
#
# You are given a string `moves` that represents the move sequence of the robot where `moves[i]` represents its `i^th` move. Valid moves are `&#39;R&#39;` (right), `&#39;L&#39;` (left), `&#39;U&#39;` (up), and `&#39;D&#39;` (down).
#
# Return `true`* if the robot returns to the origin after it finishes all of its moves, or *`false`* otherwise*.
#
# **Note**: The way that the robot is &quot;facing&quot; is irrelevant. `&#39;R&#39;` will always make the robot move to the right once, `&#39;L&#39;` will always make it move left, etc. Also, assume that the magnitude of the robot&#39;s movement is the same for each move.
#
#  
#
# **Example 1:**
#
# **Input:** moves = &quot;UD&quot;
# **Output:** true
# **Explanation**: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
#
# ```
#
# **Example 2:**
#
# **Input:** moves = &quot;LL&quot;
# **Output:** false
# **Explanation**: The robot moves left twice. It ends up two &quot;moves&quot; to the left of the origin. We return false because it is not at the origin at the end of its moves.
#
# ```
#
#  
#
# **Constraints:**
#
# 	
# - `1 &lt;= moves.length &lt;= 2 * 10^4`
# 	
# - `moves` only contains the characters `&#39;U&#39;`, `&#39;D&#39;`, `&#39;L&#39;` and `&#39;R&#39;`.
#
# ====== SOLUTION ======

class Solution:
    def judgeCircle(self, s: str) -> bool:
        i=0
        j=0
        for x in s:
            if x =="R":
                i+=1
            elif x=="L":
                i-=1
            elif x=="U":
                j-=1
            else:
                j+=1
        return i==0 and j==0
