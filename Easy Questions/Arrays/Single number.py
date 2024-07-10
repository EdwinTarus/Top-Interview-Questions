class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        count = {}
        for item in nums:
            if item in count:
                count[item] +=1
            else:
                count[item] = 1
        
        for i, num in enumerate(nums):
            if count[num] == 1:
                return nums[i]
