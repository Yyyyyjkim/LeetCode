from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s) == Counter(t):
            return True
        else:
            return False

s = "anagram"
t = "nagaram"

s = "rat"
t = "car"