class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        else:
            for i in range(1,len(s)+1):
                stop = False
                for k in range(len(s)-i+1):
                    if len(set(s[k:(k+i)]))==i:
                        stop = True
                        break
                if stop == False:
                    return i-1
                if (i==len(s)) and (stop==True):
                    return i

s = "abcabcbb"
s = "abcde"
s = ""