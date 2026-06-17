class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
        unordered_set<int> s;
        for(int i=0;i<nums.size();i++){
            s.insert(nums[i]);
        }
        if(s.size()<=1){
            return s.size();
        }
        priority_queue<int> pq;
        for(auto itr= s.begin();itr!=s.end();itr++){
            pq.push(*itr);
        }
        int res = INT_MIN;
        vector<int> v;
        v.push_back(pq.top());
        pq.pop();
        while(!pq.empty()){
            int tempCnt = 1;
            while(!pq.empty() && (v.back()-pq.top()==1)){
                tempCnt++;
                v.push_back(pq.top());
                pq.pop();
                // continue;
            }
            if(!pq.empty()){
                v.push_back(pq.top());
                pq.pop();
                // tempCnt++;
            }
            res = max(res,tempCnt);
            // if(v.back()-pq.top()==1){

            // }
            // int temp = pq.top();
            // pq.pop();
            
            
        }
        return res;     
    }
};
  