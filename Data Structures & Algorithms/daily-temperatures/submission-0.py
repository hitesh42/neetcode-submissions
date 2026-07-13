class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        
        n = len(temperatures)
        res = [0]*n
        # i = 0
        stack.append((temperatures[0],0))
        for i in range(1,n):
            while (len(stack)>0) and (temperatures[i]>stack[-1][0]):
                temp = stack.pop()
                res[temp[1]] = i - temp[1]
            else:
                stack.append((temperatures[i], i))

        return res
