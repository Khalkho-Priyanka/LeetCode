class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        listed= {}

        for i,n in enumerate(nums):
            diff= target-n
            if diff in listed:
                return(listed[diff], i)
            listed[n]=i
        return