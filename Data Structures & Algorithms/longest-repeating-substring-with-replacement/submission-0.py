class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        maxF = 0
        l , r = 0,0
        res = 0
        for c in s:
            if c in cnt:
                cnt[c]+=1
            else:
                cnt[c] = 1
            maxF = max(maxF, cnt[c])
            while (r-l+1) - maxF > k: 
                cnt[s[l]]-=1
                l+=1
            # print(f"{r}-{l}")
            res = max(res, r-l+1)
            r+=1

        return res
