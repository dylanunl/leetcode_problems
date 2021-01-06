class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #not in-place
        non_zero = []
        
        for num in nums:
            if num != 0:
                non_zero.append(num)
                
        for i in range(len(non_zero)):
            nums[i] = non_zero[i]
            
        for i in range(len(non_zero),len(nums)):
            nums[i] = 0