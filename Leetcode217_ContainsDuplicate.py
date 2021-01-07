class Solution:
    ###approach 1
    def containsDuplicate(self, nums):
        """
        用enumerate的function把list里的element都存到dict里，如果已经存在于dict就是有重复，遍历完一遍都没有重复就返回False
        """
        counter = {}
        for i, num in enumerate(nums):
            if num not in counter:
                counter[num] = i
            else:
                return True
        return False

###approach 2
    def containsDuplicate2(self, nums):
        """
        用collection里的Counter，数完之后用.values()来判定是否有出现次数大于等于2
        """
        from collections import Counter
        nums_count = Counter(nums)
        for i in nums_count.values():
            if i>=2:
                return True
        
        return False

###approach 3
    def containsDuplicate3(self, nums):
        """
        用set来比较nums的长度
        """
        if len(set(nums)) == len(nums):
            return False
        return True

###approach 4
    def containsDuplicate4(self, nums):
        """
        先排序，然后做对比
        """
        sorted_nums = sorted(nums)
        for i in range(len(nums)-1):
            if sorted_nums[i] ==sorted_nums[i+1]:
                return True
        return False
    
#         nums_sort = sorted(nums)
#         for i, _ in enumerate(nums_sort[:-1]):
#             if nums_sort[i] == nums_sort[i + 1]:
#                 return True
        
#         return False
test = Solution()
nums = [1,2,3]
print(test.containsDuplicate(nums))