class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1_map = {}
        window = {}

        for char in s1:
            s1_map[char] = 1 + s1_map.get(char, 0)

        l = 0

        for r in range(len(s2)):
            char = s2[r]
            window[char] = 1 + window.get(char, 0)

            # Keep window size equal to len(s1)
            if r - l + 1 > len(s1):
                left_char = s2[l]
                window[left_char] -= 1

                if window[left_char] == 0:
                    del window[left_char]

                l += 1

            if window == s1_map:
                return True

        return False
