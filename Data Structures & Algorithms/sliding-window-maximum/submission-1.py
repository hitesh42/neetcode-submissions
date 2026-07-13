class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # running_max = float("-infinity")
        # running_max_next = float("-infinity")
        res = []
        temp = []
        l, r = 0,0
        n = len(nums)
        for l in range(1):
            while (r<(l+k)) and (r<n):
                heapq.heappush(temp,-nums[r])
                r+=1
            # print(temp)
            res.append(-temp[0])

        for l in range(1, n-k+1):
            if (-nums[l-1]) == temp[0]:
                heapq.heappop(temp)
            else:
                temp.remove(-nums[l-1])
            while (r<(l+k)) and (r<n):
                heapq.heappush(temp,-nums[r])
                r+=1
            # print(temp)
            res.append(-temp[0])
        return res

            #     if running_max<nums[r]:
            #         running_max_next = running_max
            #         running_max = nums[r]
                    
            #     elif running_max_next<nums[r]:
            #         running_max_next = nums[r]

            #     # if nums[r]
            #     # if running_max_next>running_max:
            #     #     running_max = running_max_next
            #     #     running_max_next 
            #     # running_max = max(running_max, nums[r])
            #     print(running_max_next)
            #     print(running_max)
            #     r+=1
            # if 
        
        
            # if (l-1)>0 :
                
