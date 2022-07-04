class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        allnums = [i for i in range(1, n+1) if i not in nums]
        return allnums