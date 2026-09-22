class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            cut = set(s)
            for c in cut:
                if s.count(c) == t.count(c):
                    continue
                else:
                    return False
            return True
        else:
            return False
