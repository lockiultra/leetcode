class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_str = set()
        max_len = 0
        for i in range(len(s)):
            for sym in s[i:]:
                if sym not in sub_str:
                    sub_str.add(sym)
                else:
                    break
            if len(sub_str) > max_len:
                max_len = len(sub_str)
            sub_str = set()
        return max_len