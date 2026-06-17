class Solution {
public:

    string encode(vector<string>& strs) {
        string res = "";
        for(int i=0;i<strs.size();i++){
            res+= to_string(strs[i].length()) + "#" +strs[i];
        }
        cout << res << endl;
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        // stringstream str(s);
        // string token;

        int i=0;
        while(i<s.length()){
            int j = s.find('#', i);
            int count = stoi(s.substr(i,j-i));
            j = j+1;
            res.push_back(s.substr(j, count));
            i = j+count;
        }

        // while(getline(str, token,',')){
        //     res.push_back(token);
        //     cout << token << "h";
        // }
        return res;
    }
};
