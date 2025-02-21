import java.util.*;
import java.io.*;


//1129
class Main {
    static int[][] board = new int[9][9];
    static int[][] squareNum = new int[9][9];
    static boolean[][] visitRow = new boolean[9][10];
    static boolean[][] visitCol = new boolean[9][10];
    static boolean[][] visitSquare = new boolean[9][10];

    public static void dfs(int r, int c) {
        if (r >= 9) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    sb.append(board[i][j]);
                }
                sb.append('\n');
            }
            System.out.println(sb.deleteCharAt(sb.length() - 1));
            System.exit(0);
        }

        if (board[r][c] != 0) {
            dfs(r + ((c+1)/9), (c+1)%9);
            return;
        }

        for (int i = 1; i <= 9; i++) {
            if (!visitRow[r][i] && !visitCol[c][i] && !visitSquare[squareNum[r][c]][i]) {
                visitRow[r][i] = true;
                visitCol[c][i] = true;
                visitSquare[squareNum[r][c]][i] = true;
                board[r][c] = i;

                dfs(r + ((c+1)/9), (c+1)%9);

                visitRow[r][i] = false;
                visitCol[c][i] = false;
                visitSquare[squareNum[r][c]][i] = false;
                board[r][c] = 0;
            }
        }
    }


    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int idx = 0;
        for (int j = 0; j < 9; j += 3) {
            for (int i = 0; i < 9; i+=3) {
                for (int r = j; r < 3 + j; r++) {
                    for (int c = i; c < 3 + i; c++) {
                        squareNum[r][c] = idx;
                    }
                }
                idx++;
            }
        }

        for (int r = 0; r < 9; r++) {
            int c = 0;
            char[] arr = bf.readLine().toCharArray();
            for (char v : arr) {
                int value = v - '0';
                board[r][c] = value;
                if (value != 0) {
                    visitRow[r][value] = true;
                    visitCol[c][value] = true;
                    visitSquare[squareNum[r][c]][value] = true;
                }
                c++;
            }
        }
        dfs(0, 0);
    }

    // 걍 띄워쓰기 기준으로 다 하나씩 숫자 입력받는 듯?
    private static int read() throws Exception {
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32) {
            n = (n << 3) + (n << 1) + (c & 15);
        }
        return n;
    }
}