from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_count = Counter(list(s))
        target = [list(s_count.keys())[i] for i in range(len(s_count)) if list(s_count.values())[i]==1]
        result = [s.index(i) for i in target]
        if len(result) > 0:
          return min(result)
        else:
          return -1

s = "leetcode"
s = "loveleetcode"