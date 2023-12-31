
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {} #O(s) space
        
        for c in list(s.replace(' ','')): #O(s)
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        
        for c in list(t.replace(' ','')): #O(t)
            if c in dic and dic[c] != 0:
                dic[c] -= 1
            else:
                return False
        
        for c in dic: #O(t)
            if dic[c] > 0:
                return False
        return True
    

testCases = [
    ('anagram','nagaram',True),
    ('rat','rat',False),
]


s = Solution()

for test in testCases:
    assert s.isAnagram(test[0],test[1]) == test[2], f"{test[0]} {test[1]} Should return {test[2]}" 

print("all casses pass")
