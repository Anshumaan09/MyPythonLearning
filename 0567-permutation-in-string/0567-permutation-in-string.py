from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        left = 0
        s1_counter = Counter(s1)
        window_size = len(s1)
        window_curr = Counter()

        for right in range(len(s2)):
            window_curr[s2[right]] += 1

            if right - left + 1 > window_size:
                left_char = s2[left]
                window_curr[left_char] -= 1

                if window_curr[left_char] == 0:
                    del window_curr[left_char]
                
                left += 1
            
            if window_curr == s1_counter:
                return True
        
        return False