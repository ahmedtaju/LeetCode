class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n,l,r = len(s), 0, 0
        arr = []
        maxSize = 0
        while r<n:
            if s[r] in arr:
                arr.remove(s[l])
                l+=1
            else:
                arr.append(s[r])
                r+=1
                maxSize = max(maxSize, r-l)
        return maxSize

