class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = {}
        
        for i in range(len(s)):
            m[s[i]] = i
        
        end = 0
        res = []
        start = 0
        for i in range(len(s)):
            end = max(end,m[s[i]])
            if i == end:
                res.append(end-start + 1)
                start = end + 1
        
        return res