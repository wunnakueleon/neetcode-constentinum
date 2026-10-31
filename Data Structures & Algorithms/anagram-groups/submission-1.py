class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        anagram_check = {}
        count = 0

        for each_word in strs:
            if str(sorted(each_word)) in anagram_check:
                list_position = anagram_check.get(str(sorted(each_word)))
                output[list_position].append(each_word)
            else:
                anagram_check[str(sorted(each_word))] = count
                output.append([])
                output[count].append(each_word)
                count += 1

        return output

        