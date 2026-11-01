class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = {}
        values = [[] for each_list in range(len(nums)+1)]
        top_k_list = []
        count = 0

        for each_int in nums:
            if each_int in dict_nums:
                dict_nums[each_int] += 1
            else:
                dict_nums[each_int] = 1
        
        for each_dict_num in dict_nums:
            values[dict_nums[each_dict_num]].append(each_dict_num)

        for val in values[::-1]:
            top_k_list += val 

        return top_k_list[:k]


        