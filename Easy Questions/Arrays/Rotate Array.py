class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # rotate the entire array
        l = 0
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        # Rotate the first k elements
        k = k % len(nums)
        l, r = 0, k-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        # rotate the rest of the elements
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
