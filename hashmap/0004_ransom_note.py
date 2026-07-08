class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        freq = {}
        for ch in magazine:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        
        for ch in ransomNote:
            if ch not in freq or freq[ch] == 0:
                return False
            
            freq[ch]-=1

        return True