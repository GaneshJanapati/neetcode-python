class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final=[]
        seen =[]
        for i in range(0,len(strs)):
            if i in seen:
                continue
            seen.append(i)
            mid =[strs[i]]
            for j in range(i+1,len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    mid.append(strs[j])
                    seen.append(j)
            final.append(mid)
        return final