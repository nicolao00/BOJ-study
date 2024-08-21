import java.util.*;
import java.io.*;

class Main {
    static int[][] board;
    static int[][] dp;
    static int R;
    static int C;
    static int K;

    static void makeSums() {
        for (int r = 1; r <= R; r++) {
            for (int c = 1; c <= C; c++) {
                dp[r][c] = board[r-1][c-1] + dp[r-1][c] + dp[r][c-1] - dp[r-1][c-1];
            }
        }
    }


    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        board = new int[R][C];
        dp = new int[R+1][C+1];

        for (int r = 0; r < R; r++) {
            st = new StringTokenizer(bf.readLine());
            for (int c = 0; c < C; c++) {
                board[r][c] = Integer.parseInt(st.nextToken());
            }
        }
        makeSums();

        StringBuilder sb = new StringBuilder();
        K = Integer.parseInt(bf.readLine());
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(bf.readLine());
            int[] rect = new int[4];
            for (int j = 0; j < 4; j++) {
                rect[j] = Integer.parseInt(st.nextToken());
            }
            sb.append(dp[rect[2]][rect[3]] - dp[rect[0]-1][rect[3]] - dp[rect[2]][rect[1]-1] + dp[rect[0]-1][rect[1]-1]);
            sb.append('\n');
        }
        System.out.println(sb.toString());
    }
}