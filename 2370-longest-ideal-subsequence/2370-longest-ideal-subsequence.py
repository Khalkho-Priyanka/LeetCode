class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        d = [0] * 26

        for i in map(lambda i: ord(i) - ord("a"), s) : (d[i])= max(d[max(i-k,0): i+k+1])+1
        
        return max(d)