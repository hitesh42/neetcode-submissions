class Solution:
    def trap(self, height: List[int]) -> int:
        # maxCurr = 0
        # i, j = 0, 1
        # n = len(height)
        # maxArea = height[i]
        # while j<n:
        #     area = min(height[i], height[j])*(j-i-1)
        #     maxArea += area
        #     maxCurr = max(height[j], maxCurr)
        #     if height[j]<=maxCurr:
        #         i = j
        #         j = i+1
        #     else:
        #         j+=1
        # maxBar = max(height)
        n = len(height)
        suffix = [0]*(n+1)
        prefix = [0]*(n+1)
        i = 0
        for i in range(n):
            prefix[i+1] = max(prefix[i],height[i])
            suffix[n-i-1] = max(suffix[n-i], height[n-i-1])
        res = 0
        for i in range(n):
            res += (min(prefix[i+1], suffix[i])-height[i])

        return res



        # return max(height)



