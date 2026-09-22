class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        mainHash = {}
        for s in strs:
            counts = []
            for l in letters:
                counts.append(s.count(l))
            try:
                mainHash[str(counts)].append(s)
            except:
                mainHash[str(counts)] = [s]

        final = [] 
        for i in mainHash.values():
            final.append(i)
        return final