class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size()!=t.size()){
            return false;
        }
        unordered_map<char, int> m;
        for(int i=0;i<s.size();i++){
            if(m.find(s[i])==m.end()){
                m[s[i]] = 1;
            }else{
                m[s[i]]++;
            }
        }
        for(int i=0;i<t.size();i++){
            if(m.find(t[i])!=m.end()){
                m[t[i]] -= 1;
            }
        }
        int sum = 0;
        for(auto itr = m.begin();itr!=m.end();itr++){
            cout << itr-> first << itr->second << endl;
            if(itr->second < 0){
                return false;
            }
            sum += itr->second;
        }
        if(sum==0){
            return true;
        }else{
            return false;
        }
    }
};
