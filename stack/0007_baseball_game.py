class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack =[]
        for ch in operations:
            if ch == "D":
                x = (stack[-1])*2
                stack.append(x)
            elif ch == "+":
                y = (stack[-1])+(stack[-2])
                stack.append(y)
            elif ch == "C":
                stack.pop()
            else:
                stack.append(int(ch))
        
        return sum(stack)
