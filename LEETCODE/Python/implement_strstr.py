class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        else:
            len_needle = len(needle)
            len_haystack = len(haystack)
            for i in range(len_haystack - len_needle + 1):
                j = 0
                while j < len_needle and haystack[i+j] == needle[j]:
                    j += 1
                if j == len_needle:
                    return i
            return -1