class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        def get_min_two(row):
            two_small= []
            for val, idx in row:
                if len(two_small) < 2:
                    two_small.append((val, idx))
                elif two_small[1][0]> val:
                    two_small.pop()
                    two_small.append((val, idx))
                two_small.sort()
            return two_small
        
        N= len(grid) 
        first_row= [(val, idx) for idx, val in enumerate(grid[0])]
        dp= get_min_two(first_row)
        for i in range(1, N):
            next_dp= []
            for curr_c in range(N):
                curr_val= grid[i][curr_c]
                min_val= float("inf")
                for prev_val, prev_c in dp:
                    if curr_c != prev_c:
                        min_val= min(min_val, curr_val + prev_val)
                next_dp.append((min_val, curr_c))
                next_dp= get_min_two(next_dp)
            dp= next_dp 
        return min([val for val, idx in dp])
        
        
        