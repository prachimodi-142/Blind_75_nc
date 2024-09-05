class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split()

        rev_words = reversed(words)

        result = ' '.join(rev_words)

        return result