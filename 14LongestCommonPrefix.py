class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        min_len = min([len(arr) for arr in strs])
        is_eq = True

        for i in range(min_len):
            prev = strs[0][i]
            for arr in strs[1:]:
                if arr[i] != prev:
                    is_eq = False
                    break
                else:
                    prev = arr[i]
            if is_eq:
                prefix += prev
            else:
                break
        return prefix