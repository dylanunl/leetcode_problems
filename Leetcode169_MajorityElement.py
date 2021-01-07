
class Solution:
    ###approach 1
    def majorityElement(self, nums):
        from collections import Counter
        """
        老办法用Counter然后取most_common(1)
        """
        nums_count = Counter(nums)
        nums_one = nums_count.most_common(1)
        return nums_one[0][0]

        # d = {}
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] not in d:
        #         d[nums[i]] = 1
        #     else:
        #         d[nums[i]] +=1
        # print(d)
        # a, b = max((a,b) for b,a in d.items())
        # return b
    ###approach 2
    def majorityElement2(self, nums):
        """
        我们一直有一个条件没有使用众数是指在数组中出现次数大于⌊ n/2 ⌋ 的元素。那么问题就很容易了，
        我们可以先将nums排序，然后返回中间元素的值即可（众数的个数大于一半，排好序的nums中间元素一定是众数）
        """
        nums.sort()
        return nums[len(nums)//2] 

    ###approach 3
    def majorityElement3(self, nums):
        """
        摩尔算法
        """
        m , c = 0,0
        for i in range(len(nums)):
            if c ==0:
                m = nums[i]
                c = 1
            elif m == nums[i]:
                c+=1
            else:
                c-=1
        counter  = 0
        for num in nums:
            if num ==m:
                counter+=1
        if counter < len(nums)//2:
            return -1
        else:
            return m

test = Solution()
nums = [1,1,2,2,2,3]
print(test.majorityElement(nums))