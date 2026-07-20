class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        left = 0
        right = n-1

        while left<right:
            sum = numbers[left]+numbers[right]

            if sum == target:
                return left+1 , right+1

            elif sum>target:
                right-=1
            else:
                left+=1