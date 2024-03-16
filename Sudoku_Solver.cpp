class Solution {
    bool row[9][10]{};
    bool col[9][10]{};
    bool box[9][10]{};

    bool canPlace(int i,int j,int a){
        int b = (i/3)*3 + (j/3);
        if( row[i][a] || col[j][a] || box[b][a]){
            return false;
        }   
        else return true;
    }
    void place (int i , int j ,int a){
        row[i][a]=true;
        col[j][a]=true;
        int b = (i/3)*3 + (j/3);
        box[b][a]=true;
    }
    void remove(int i ,int j,int a){
        row[i][a]=false;
        col[j][a]=false;
        int b = (i/3)*3 + (j/3);
        box[b][a]=false;
    }

    bool RightBoard(vector<vector<char>> &board,int i=0,int j=0){
        if(i>8) return true;
        if(board[i][j]=='.'){
            int a = 1;
            while(a<10){
                if(canPlace(i,j,a)){
                    place(i,j,a);

                    bool b=true;
                    if(j==8){
                        b = RightBoard(board,i+1,0);
                    }   else{
                        b = RightBoard(board,i,j+1);
                    }
                    if(b){
            // cout<<i<<' '<<j<<' '<<a<<endl;
                        board[i][j]= '0'+a;
                        return true;
                    }   
                    remove(i,j,a);
                }
                a++;
            }
            return false;
        }
        else{
            bool b;
            if(j==8){
                b = RightBoard(board,i+1,0);
            }   else{
                b = RightBoard(board,i,j+1);
            }
            return b;
        }
    }
    void addElement(vector<vector<char>> & board){
        // Add All member to array ...
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                if(board[i][j]!='.'){
                    int a = board[i][j]-'0';
                    place(i,j,a);
                }
            }
        }
    } 
public:
    void solveSudoku(vector<vector<char>>& board) {
        addElement(board);
        // Call recurssion......
        bool Ans = RightBoard(board);
    }
};