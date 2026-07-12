class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        i, j = 0,0
        n = len(s)
        res = 0
        for c in s:
            while c in st:
                st.remove(s[i])
                i+=1
            st.add(c)
            
            res = max(res, j-i+1)
            j+=1
        return res
