class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        main_hm = {}
        for i in range(len(strs)):
            hm = {}
            for j in range(len(strs[i])):
                char = strs[i][j]

                if char in hm:
                    hm[char] += 1
                else:
                    hm[char] = 1

            key = tuple(sorted(hm.items()))    
            
            if key in main_hm:
                main_hm[key].append(strs[i])
            else:
                main_hm[key] = [strs[i]]
        
        for key in main_hm:
            res.append(main_hm[key])

        return res



                