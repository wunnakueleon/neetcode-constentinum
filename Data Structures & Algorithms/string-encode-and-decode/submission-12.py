class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        first_space = True

        if strs == []:
            return "empty"

        for each_str in strs:
            if not first_space:
                string += "lee" + each_str
            else:
                string += each_str
                first_space = False
            
        return string

    def decode(self, s: str) -> List[str]:

        if s == "empty":
            return []

        return s.split("lee")
