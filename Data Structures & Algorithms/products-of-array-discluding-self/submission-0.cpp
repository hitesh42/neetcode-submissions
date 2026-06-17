class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n  = nums.size();
        vector<int> a(n,1),b(n,1);
        for(int i =1;i<nums.size();i++){
            // a.push_back(1)
            a[i] = nums[i-1]*a[i-1];
        }
        for(int i = n-2;i>=0;i--){
            // a.push_back(1)
            b[i] = nums[i+1]*b[i+1];
        }
        vector<int> res(n,1);
        for(int i=0;i<n;i++){
            res[i] = a[i]*b[i];
        }
        return res;
    }
};
