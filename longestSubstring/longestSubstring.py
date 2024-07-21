class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        times = 0
        maxTimes = 0
        lastc = None

        for c in s:
            if (lastc == c): times = 0

            times += 1
            if (maxTimes < times): maxTimes = times

            lastc = c

        return maxTimes
