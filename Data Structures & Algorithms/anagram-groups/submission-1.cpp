class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> anagrams;
        vector<string> hash;
        for(string& s:strs){
            vector<int> v(26,0);
            for(char c:s){
                int index = c - 'a';
                // cout << index;
                // cout << v[index]<< endl;
                v[index]++;
                // cout << v[index] << endl;
            }
            // cout << endl;
            string key;
            for(int count:v){
                // cout << count;
                key += to_string(count) + ',';
            }
            cout << endl;
            //cout << key << endl;
            anagrams[key].push_back(s);
        }
        vector<vector<string>> res;
        for(auto& [k,val]:anagrams){
            res.push_back(val);
        }
        // for(int i=0;i<strs.size();i++){
        //     unordered_map<char, int> m;
        //     for(int j=0;j<strs[i].size();j++){
        //         if(m.find(strs[i][j]) == m.end()){
        //             m[strs[i][j]] = 1;
        //         }else{
        //             m[strs[i][j]]++;
        //         }
        //     }
        //     if(anagrams.find(m) == m.end()){
        //         vector<int> v;
        //         v.push_back(i);
        //         anagrams[m] = v;
        //     }else{
        //         anagrams[m].push_back(i);
        //     }
        // }
        // vector<vector<string>> res;
        // for(auto it = anagrams.begin();it!=anagrams.end();it++){
        //     res.push_back(it->second);
        // }
        return res;
    }
};
