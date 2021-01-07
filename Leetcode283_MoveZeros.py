class Solution:
    ###approach 1
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        我们首先想到的做法是：遍历一遍数组nums，将非0元素添加到一个新建立的数组nonZeroElements中，
        然后将nonZeroElements中的元素copy到nums的最前面，对nums后面的元素赋值0即可。
        """
        non_zero = []
        
        for num in nums:
            if num != 0:
                non_zero.append(num)
                
        for i in range(len(non_zero)):
            nums[i] = non_zero[i]
            
        for i in range(len(non_zero),len(nums)):
            nums[i] = 0

    ###approach 2
    def moveZeroes2(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        我们可以使用一个变量k记录位置，我们通过遍历nums数组，将不为0的元素依次复制到nums的前面，并且记录我们复制了多少个元素，对len(nums)-k的元素置0即可。
        """
        k = 0
        for num in nums:
            if num !=0 :
                nums[k] = num
                k+=1
        for i in range(k, len(nums)):
            nums[i] = 0

    ###approach 3
    def moveZeroes3(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        通过上面的方法，我们将算法的空间复杂度降到了O(1)级别，而算法的时间复杂度依旧是O(n)级别。
        当然我们这里有一个更pythonic的做法,但是从效率上远不及前面的做法。
        """
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)

    
    ###approach 4
    def moveZeroes4(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        我们看到上面的做法都是对非0元素和0元素分开考虑，那们我们可不可以对这两种元素同时考虑呢？我们通过不断的交换非0元素和0元素之间的位置做到这一点。
        """
        k = 0
        for i, num in enumerate(nums):
            if num != 0 :
                nums[i], nums[k] = nums[k], nums[i]
                k+=1


    ###approach 5
    def moveZeroes5(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        上面的代码比之前的简洁了不少，但是依然还有可优化的空间。如果我们的数组全部是非0元素的话，上面代码就会对所有非0元素自己交换一次。所有可以有如下改进：
        """
        k = 0
        for i, num in enumerate(nums):
            if num != 0:
                if i!= k:
                    nums[i],nums[k] = nums[k],nums[i]
                k+=1
                    

move = Solution()
nums=[1,0,0,2,3]
move.moveZeroes4(nums)
print(nums)
