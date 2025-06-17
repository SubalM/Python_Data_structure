

# Method 1:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths are different, they cannot be anagrams.
        if len(s) != len(t):
            return False

        # Create a frequency array for lowercase English letters (26 characters).
        # Initialize all counts to 0.
        char_counts = [0] * 26

        # Populate frequencies for string s
        for char in s:
            # Convert character to an integer index (0-25)
            # 'a' -> 0, 'b' -> 1, ..., 'z' -> 25
            char_counts[ord(char) - ord('a')] += 1
        # If char is 'a':
        # ord('a') - ord('a') = 97 - 97 = 0
        # Result: 0

        # If char is 'b':
        # ord('b') - ord('a') = 98 - 97 = 1
        # Result: 1

        # If char is 'c':
        # ord('c') - ord('a') = 99 - 97 = 2
        # Result: 2

        # ...and so on...

        # If char is 'z':
        # ord('z') - ord('a') = 122 - 97 = 25
        # Result: 25
        # Decrement frequencies for string t
        for char in t:
            # If a character in t is not found in s (or its count goes below zero),
            # then they are not anagrams.
            index = ord(char) - ord('a')
            char_counts[index] -= 1
            # Optional optimization: if char_counts[index] becomes negative,
            # it means 't' has more of this character than 's', so it can't be an anagram.
            # This can short-circuit the loop early.
            # if char_counts[index] < 0:
            #     return False

        # After processing both strings, all counts in char_counts should be 0
        # if s and t are anagrams.
        for count in char_counts:
            if count != 0:
                return False

        return True

# Method 2:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Sorting O(nlogn+mlogm)
        # if len(s) != len(t):
        #     return False

        # return sorted(s) == sorted(t)

        # Hash Map O(n+m)
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0) #count the number of partcular character in the list

        return count_s == count_t


sol = Solution()
s = 'racecar'
t = 'carrace'

print(sol.isAnagram(s, t))