class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_list = defaultdict(list)
        
        for word in strs:
            count = [0] * 26 # from a to z
            for each_letter in word:
                count[ord(each_letter) - ord('a')] += 1
            
            dict_list[tuple(count)].append(word)

        
            

        return list(dict_list.values())

        