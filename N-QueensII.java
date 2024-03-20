class Solution {
    public int totalNQueens(int n) {
        char [][] board = new char [n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                board[i][j] = '.';
            }
        }
        // List<List<String>> ans = new ArrayList<>();
        boolean [] upperDiag = new boolean [2 * n - 1];
        boolean [] lowerDiag = new boolean [2 * n - 1];
        boolean [] leftrow = new boolean [n];
        return f(0,board,upperDiag,lowerDiag,leftrow);
        // return ans.size(); 
    }

    public int f(int col,char [][] board,boolean [] upperDiag, boolean [] lowerDiag, boolean [] leftrow){

        if(col == board.length){
            return 1;
        }

        int result = 0;
        for(int row = 0; row < board.length; row++){
            if(!leftrow[row] && !upperDiag[board.length - 1 + col - row] && !lowerDiag[row + col]){
                board [row][col] = 'Q';
                leftrow[row] = true;
                upperDiag[board.length - 1 + col - row] = true;
                lowerDiag[row + col] = true;
                result += f(col+1,board,upperDiag,lowerDiag,leftrow);
                board [row][col] = '.';
                leftrow[row] = false;
                upperDiag[board.length - 1 + col - row] = false;
                lowerDiag[row + col] = false;
            }
        }
        return result;
    }
}