// =======================
// 980. Unique Paths III
// =======================
// Difficulty: Hard
//
// You are given an `m x n` integer array `grid` where `grid[i][j]` could be:
//
// 	
// - `1` representing the starting square. There is exactly one starting square.
// 	
// - `2` representing the ending square. There is exactly one ending square.
// 	
// - `0` representing empty squares we can walk over.
// 	
// - `-1` representing obstacles that we cannot walk over.
//
// Return *the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once*.
//
//  
//
// **Example 1:**
//
// []
//
// **Input:** grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
// **Output:** 2
// **Explanation:** We have the following two paths: 
// 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
// 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
//
// ```
//
// **Example 2:**
//
// []
//
// **Input:** grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
// **Output:** 4
// **Explanation:** We have the following four paths: 
// 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
// 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
// 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
// 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
//
// ```
//
// **Example 3:**
//
// []
//
// **Input:** grid = [[0,1],[2,0]]
// **Output:** 0
// **Explanation:** There is no path that walks over every empty square exactly once.
// Note that the starting and ending square can be anywhere in the grid.
//
// ```
//
//  
//
// **Constraints:**
//
// 	
// - `m == grid.length`
// 	
// - `n == grid[i].length`
// 	
// - `1 &lt;= m, n &lt;= 20`
// 	
// - `1 &lt;= m * n &lt;= 20`
// 	
// - `-1 &lt;= grid[i][j] &lt;= 2`
// 	
// - There is exactly one starting cell and one ending cell.
//
// ====== SOLUTION ======

class Solution {
    int ans = 0;
    int r,c;
    public int uniquePathsIII(int[][] grid) {
        r = grid.length;
        c = grid[0].length;

        int sx = 0;
        int sy = 0;
        int count =0;

        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){

                if(grid[i][j]!=-1){
                    count++;
                }

                if(grid[i][j]==1){
                    sx=i;
                    sy=j;
                }
            }
        }

        backtrack(grid,sx,sy,count);

        return ans;
    }

    void backtrack(int[][] grid,int x, int y,int count){

        if( x<0 || y<0 || x>=r || y>=c || grid[x][y]==-1 || grid[x][y]==-2){
            return;
        }

        if( grid[x][y]==2){
            if(count==1){
                ans+=1;
            }
        }

        int temp = grid[x][y];

        grid[x][y]=-2;

        backtrack(grid,x+1,y,count-1);
        backtrack(grid,x-1,y,count-1);
        backtrack(grid,x,y+1,count-1);
        backtrack(grid,x,y-1,count-1);

        grid[x][y]=temp;
    }
}
