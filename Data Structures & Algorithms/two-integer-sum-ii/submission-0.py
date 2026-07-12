class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        temp = {}
        idx = 0
        res = []
        for n in numbers:
            if (target-n) not in temp:
                temp[n] = idx
            else:
                # print(temp[target-n])
                # print(temp[n])
                return [temp[target-n]+1, idx+1]
            idx+=1