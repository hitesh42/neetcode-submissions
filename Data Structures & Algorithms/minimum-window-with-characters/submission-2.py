class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = Counter(t)
        window = {}
        have =0
        need = len(cnt)
        l = 0
        n = len(s)
        res = [-1,-1]
        reslenMax = float("infinity")
        for r in range(n):
            
            window[s[r]] = 1 + window.get(s[r],0)
            if s[r] in cnt and cnt[s[r]] == window[s[r]]:
                have+=1

            while need==have:
                if (r-l+1)<reslenMax:
                    res = [l,r]
                    reslenMax = min(reslenMax, r-l+1)
                window[s[l]]-=1
                if s[l] in cnt and window[s[l]]<cnt[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if res!=float("infinity") else ""

            # while c in 
            