class Solution:
    ###approach 1
    def missingNumber(self, nums):
        """
        题目要求是in-place,但我用的是out of place。这是我首先想到的用counter去计算
        """
        from collections import Counter
        nums_count = Counter(nums)
        nums_keys = nums_count.keys()
        length = len(nums_keys)
        max_keys = max(nums_keys)
        for i in range(length+1):
            if i not in nums_keys:
                return i
    
    ###approach 2
    def missingNumber2(self, nums):
        """
        要用//，因为只用/，会得到2.0小数点，用//可以避免小数点出现
        我们可以将所以数加起来得到一个缺失一个数字的和，如果我们不缺任何数字的话，所有数组的和应该是( 1 + n ) n / 2 (1+n)n/2(1+n)n/2。所以根据二者之差就可以得到结果
        """
        n = len(nums)
        sums1 = n*(1+n)//2
        sums2 = sum(nums)
        return sums1-sums2

    ###approach 3
    def missingNumber3(self, nums):
        """
        用XOR ^异或的方式来求得唯一没有被消除的element,也就是缺失的element
        """
        result = len(nums)
        for i in range(len(nums)):
            result ^= i^nums[i]
        return result

nums = [1,0,3]
test = Solution()
print(test.missingNumber3(nums))