class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n-1

        while left<=right:

            mid = (left+right)//2

            if nums[mid] == target:
                return mid

            elif target>nums[mid]:
                left = mid+1

            else:
                right = mid-1

        return -1