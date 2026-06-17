class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int n = board.size();
        int m = board[0].size();
        unordered_set<int> row[n];
        unordered_set<int> col[m];
        unordered_set<int> subMat[n];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                // vector<int> r(n, 0);
                // vector<int> c(m,0);
                // int subRow = (i/3)*3;
                // int subCol = (j/3)*3;
                if(board[i][j] != '.'){
                    int num = (board[i][j] - '0');

                    if(row[i].find(num) != row[i].end()){
                        return false;
                    }
                    row[i].insert(num);

                    if(col[j].find(num) != col[j].end()){
                        return false;
                    }
                    col[j].insert(num);

                    int idx = (i/3)*3 + (j/3);

                    if(subMat[idx].find(num) != subMat[idx].end()){
                        return false;
                    }
                    subMat[idx].insert(num);
                }
            }
        }
        return true;
    }
};
