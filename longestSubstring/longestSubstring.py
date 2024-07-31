class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 : return 0
        max = 1
        for i in range(len(s)) :
            j = i + 1;
            while (j < len(s)) :
                if i == 0 : cur = 1
                else : cur = 2
                if (s[i] == s[j]) :
                    break
                else :
                    cur += 1
                    if (cur > max) : max = cur

                    j += 1

        return max
