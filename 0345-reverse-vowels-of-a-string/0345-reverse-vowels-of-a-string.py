class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = []
        pos = []
        result = list(s)

        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                vowels.append(s[i])
                pos.append(i)

        v2 = list(reversed(vowels))

        for i in range(len(pos)):
            result[pos[i]] = v2[i]

        return "".join(result)