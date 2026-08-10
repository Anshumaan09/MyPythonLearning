class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        # If string is too short, it cannot be valid
        if len(s) < k:
            return 0

        # Count frequency of each character
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        # Find a character that occurs less than k times
        for char in s:
            if freq[char] < k:

                # Split around this bad character
                left = s.split(char)

                # Solve every part separately
                max_length = 0

                for part in left:
                    max_length = max(
                        max_length,
                        self.longestSubstring(part, k)
                    )

                return max_length

        # If no bad character exists,
        # the entire string is valid
        return len(s)