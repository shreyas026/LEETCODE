class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zc = 0
       
        for i in range(len(nums)):
            if nums[i] == 0:
                zc += 1
            else:
                nums[i - zc] = nums[i]
        
        for i in range(len(nums) - zc, len(nums)):
            nums[i] = 0