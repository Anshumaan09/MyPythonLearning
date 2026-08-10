class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        var_present = set()
        max_length = 0

        for end in range(len(s)):
            while s[end] in var_present:
                var_present.remove(s[start])
                start +=1

            var_present.add(s[end])

            current_len = end - start + 1
            max_length = max(max_length, current_len)
        return max_length

