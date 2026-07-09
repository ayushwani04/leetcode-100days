class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        pairs = {
            ")" : "(",
            "]" : "[",
            "}" : "{" 
        }

        for ch in s:
            if ch in "([{":
                stack.append(ch)

            else:
                if not stack:
                    return False

                if pairs[ch]!=stack[-1]:
                    return False

                stack.pop()
        return not stack
         