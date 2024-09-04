class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
         # find min word size
         # join values till min
         # append rest of the word from the longest word

        result = ""
        # total_len = len(word1) + len(word2)

        min_len = min(len(word1), len(word2))

        for i in range(min_len):
            result += word1[i] + word2[i]

        if len(word1) < len(word2):
            result += word2[min_len:]

        elif len(word2) < len(word1):
            result += word1[min_len:]

        return result

        