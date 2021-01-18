from collections import Counter

class Solution:
    def customSortString(self, S: str, T: str) -> str:
      s = {i:S[i] for i in range(len(S))}
      t = Counter(T)
      result = []
      for i in range(len(s)):
        result.append(list(s.values())[i]*T.count(s[i]))
      rest = [i for i in T if i not in S]
      return "".join(result)+"".join(rest)

S = "cba"
T = "abcd"
