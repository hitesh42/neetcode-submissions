class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # st = Counter(s1)
        cnt = 0
        # s1.sort()
        s1 = "".join(sorted(s1))
        n2 = len(s2)
        n1 = len(s1)
        for l in range(n2):
            # if s2[l] in s1:
            if "".join(sorted(s2[l:l+n1])) == s1:
                return True

        # print(st)
        return False