class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
      # Solution 1
        l = 0
        for r in range(1,len(nums)):
            if nums[r] !=0:
                # l=2 r=4
                print(f"before: l : {l}, r: {r}, nums[l]: {nums[l]}, nums[r]: {nums[r]}")
                nums[l],nums[r] = nums[r],nums[l] #[1,0,3,0]
                print(f"After: l : {l}, r: {r}, nums[l]: {nums[l]}, nums[r]: {nums[r]}")
                print(nums)
                l+=1
        # Solution 2
        # for num in nums:
        #     if num == 0:
        #         nums.remove(num)
        #         nums.append(num)
