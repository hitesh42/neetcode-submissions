class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> s;
        vector<int> res;
        for(int i=0;i<nums.size();i++){
            if(s.find(target-nums[i])!=s.end()){
                res.push_back(s[target-nums[i]]);
                res.push_back(i);
                return res;
            }else{
                s.insert({nums[i],i});
            }
        }
        
    }
};
