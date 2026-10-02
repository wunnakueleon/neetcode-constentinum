class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> uniqueNums = new HashMap<>();


        for (int i = 0; i <= nums.length - 1; i++) {
            uniqueNums.merge(nums[i], 1, Integer::sum);
                
        }

        ArrayList<Integer> keySets = new ArrayList<>(uniqueNums.keySet());
        keySets.sort((a, b) -> uniqueNums.get(b) - uniqueNums.get(a));

        int[] kList = new int[k];
        for (int i = 0; i < k; i++) {
            kList[i] = keySets.get(i);
        }
        return kList;

        
    }
}
