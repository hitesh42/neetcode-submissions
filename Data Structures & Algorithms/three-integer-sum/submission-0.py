class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i, j = 0,0
        out = []
        for i in range(len(nums)):
            target = 0 - nums[i]
            temp = {}
            res = []
            for j in range(i+1, len(nums)):
                if target - nums[j] not in temp:
                    temp[nums[j]] = j
                else:
                    res.append(nums[i])
                    res.append(nums[j])
                    res.append(target-nums[j])
                    res.sort()
                    if res not in out:
                        out.append(res)
                    res = []
                    # break
                j+=1
            i+=1
            # out.append(res)
        
        return out

        