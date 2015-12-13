'''
https://leetcode.com/problems/two-sum/

'''



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        print(nums)
        print(target)

        for i in range(0, len(nums)):
            one = nums[i]
            for x in range(i, len(nums)):
                two = nums[x]
                if one+two == target:
                    #return [one, two]
                    return [i, x]
        return false



a = Solution()
b = a.twoSum([2,7,11,4], 9)
print(b)
