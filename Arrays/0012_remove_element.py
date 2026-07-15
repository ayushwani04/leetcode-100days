class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow=0
        fast=0

        if not nums:
            return 0

        while fast<len(nums):
            if nums[fast]==val:
                fast+=1

            else:
                nums[slow] = nums[fast]
                slow+=1
                fast+=1

        print(nums)
        return slow