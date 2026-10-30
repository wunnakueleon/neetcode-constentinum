class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}
        result = []
        for i in range(len(nums)):
            num_search = target - nums[i]
            if num_search in num_hash and num_hash[num_search] != i:
                result.append(num_hash[num_search])
                result.append(i)
                return result
            else:
                num_hash[nums[i]] = i
            
        return []
        