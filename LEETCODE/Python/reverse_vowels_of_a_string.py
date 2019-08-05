class Solution:
    def reverseVowels(self, s: str) -> str:
        char_list = list(s)
        index_list = []
        
        for index, char in enumerate(s):
            if char in 'aeiouAEIOU':
                index_list.append(index)
        
        for i, j in zip(index_list, index_list[::-1]):
            char_list[i] = s[j]

        return ''.join(char_list)