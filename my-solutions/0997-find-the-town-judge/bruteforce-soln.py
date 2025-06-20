class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n <= 1:
            return 1
        
        trustFrom = {}
        trustTo = {}
        for a, b in trust:
            if a not in trustFrom:
                trustFrom[a] = []
            if b not in trustFrom:
                trustFrom[b] = []
            if a not in trustTo:
                trustTo[a] = []
            if b not in trustTo:
                trustTo[b] = []

            trustFrom[a].append(b)
            trustTo[b].append(a)
        
        result = -1
        highestTrust = 0

        for key, val in trustFrom.items():
            if len(val) == 0: 
                if len(trustTo[key]) > highestTrust:
                    result = key
                    highestTrust = len(trustTo[key])

        if highestTrust < n-1:
            return -1

        return result
    