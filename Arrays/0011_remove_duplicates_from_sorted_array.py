class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow=0
        fast=1
        if not nums:
            return 0

        while fast < len(nums):
            if nums[slow]==nums[fast]:
                fast+=1

            else :
                
                slow+=1
                nums[slow]=nums[fast]
                fast+=1
        
        return slow+1