class Solution {
    public boolean isAnagram(String s, String t) {

        HashMap<Character, Integer> firsthashmap = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            firsthashmap.merge(s.charAt(i), 1, Integer::sum);
        }

        HashMap<Character, Integer> secondhashmap = new HashMap<>();
        for (int i = 0; i < t.length(); i++) {
            secondhashmap.merge(t.charAt(i), 1, Integer::sum);
        }

        return firsthashmap.equals(secondhashmap);


        

    }
}
