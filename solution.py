class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        allnums = set([i for i in range(1, n+1)])
        nums = set(nums)
        return list(allnums.difference(nums))

print(Solution().findDisappearedNumbers([1,1]))