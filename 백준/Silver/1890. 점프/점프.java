import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main{
    public static class Tuple {
        public int r;
        public int c;
        public Tuple(int r, int c){
            this.r = r;
            this.c = c;
        }
    }
    public static void main(String args[]) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        int[][] board = new int[N][N];
        long[][] dp = new long[N][N];
        dp[0][0] = 1;

        for(int i=0;i<N;i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            for(int j=0;j<N;j++){
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int r = 0; r < N; r++) {
            for (int c =0; c < N; c++) {
                if (dp[r][c] == 0) continue;
                if (r == N-1 && c == N-1) break;
                int[][] rc = {{r + board[r][c], c}, {r, c + board[r][c]}};
                for (int i = 0; i<2; i++) {
                    if (0 <= rc[i][0] && rc[i][0] < N && 0 <= rc[i][1] && rc[i][1] < N) {
                        dp[rc[i][0]][rc[i][1]] += dp[r][c];
                    }
                }
            }
        }
        System.out.println(dp[N-1][N-1]);
    }
}