class Solution {
public:
    struct compare{
        bool operator()(pair<int,int> a, pair<int,int> b){
            return a.second<b.second;
        }
    };
    // bool comp(pair<int,int> a, pair<int,int> b){
    //     return a.second>b.second;
    // }
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> m;
        
        priority_queue<pair<int,int>, vector<pair<int,int>>, compare> pq;

        for(int i=0;i<nums.size();i++){
            if(m.find(nums[i])==m.end()){
                m.insert({nums[i], 1});
            }else{
                m[nums[i]]++;
            }
        }

        for(auto itr = m.begin();itr!=m.end();itr++){
            pq.push(make_pair(itr->first, itr->second));
        }
        vector<int> out;
        for(int i=0;i<k;i++){
            if(!pq.empty()){
                auto num = pq.top();
                pq.pop();
                out.push_back(num.first);
            }
        }
        return out;

    }
};
