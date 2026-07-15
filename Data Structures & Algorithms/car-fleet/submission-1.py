class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        arr = [(x,y) for x,y in zip(position,speed)]
        arr.sort(reverse=True)
        for p,s in arr:
            time.append((target-p)/s)

        stack = deque()
        stack.append(time[0])
        for i in range(1,len(time)):
            if time[i]<=stack[-1]:
                continue
                # stack.pop()
                # stack.append(time[i])
            else:
                stack.append(time[i])
        print(time)
        return len(stack)    
        
        # print(arr)
        # return 0
