class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """

        trusts_someone = [False] * (n + 1)
        trusted_by = [0] * (n + 1)

        for a, b in trust:
            trusts_someone[a] = True
            trusted_by[b] += 1

        for person in range(1, n + 1):
            if not trusts_someone[person] and trusted_by[person] == n - 1:
                return person

        return -1