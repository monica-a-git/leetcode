class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps={}
        l=[]
        for i in range(len(strs)):
            ss =  "".join(sorted(strs[i]))
            if ss in maps:
                l[maps[ss]].append(strs[i])
            else:
                l.append([strs[i]])
                maps[ss]=l.index([strs[i]])
        
        return l