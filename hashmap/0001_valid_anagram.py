class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for x in s:
            if x in countS:
                countS[x]+=1
            else:
                countS[x] = 1

        for x in t:
            if x in countT:
                countT[x]+=1
            else:
                countT[x] = 1

        return countS == countT