//import java.util.*;
//import java.io.*;
//
//class Main {
//    static int[][] board;
//    static int[][] dp;
//    static int R;
//    static int C;
//    static int K;
//
//    static void makeSums() {
//        for (int r = 1; r <= R; r++) {
//            for (int c = 1; c <= C; c++) {
//                dp[r][c] = board[r-1][c-1] + dp[r-1][c] + dp[r][c-1] - dp[r-1][c-1];
//            }
//        }
//    }
//
//
//    public static void main(String[] args) throws IOException{
//        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(bf.readLine());
//        R = Integer.parseInt(st.nextToken());
//        C = Integer.parseInt(st.nextToken());
//        board = new int[R][C];
//        dp = new int[R+1][C+1];
//
//        for (int r = 0; r < R; r++) {
//            st = new StringTokenizer(bf.readLine());
//            for (int c = 0; c < C; c++) {
//                board[r][c] = Integer.parseInt(st.nextToken());
//            }
//        }
//        makeSums();
//
//        StringBuilder sb = new StringBuilder();
//        K = Integer.parseInt(bf.readLine());
//        for (int i = 0; i < K; i++) {
//            st = new StringTokenizer(bf.readLine());
//            int[] rect = new int[4];
//            for (int j = 0; j < 4; j++) {
//                rect[j] = Integer.parseInt(st.nextToken());
//            }
//            sb.append(dp[rect[2]][rect[3]] - dp[rect[0]-1][rect[3]] - dp[rect[2]][rect[1]-1] + dp[rect[0]-1][rect[1]-1]);
//            sb.append('\n');
//        }
//        System.out.println(sb.toString());
//    }
//}


import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    static int[][] dp;
    static int[][] land;

//    static void backtracking(int row, int col) {
//        for (int i = 0; i < 4; i++) {
//            if (col == i)
//                continue;
//
//            int value = dp[row-1][col] + land[row][i];
//            if (value > dp[row][i]) {
//                dp[row][i] = value;
//                if (row < land.length - 1)
//                    backtracking(row+1, i);
//            }
//        }
//    }

    static void bfs() {
        Queue<int[]> q = new ArrayDeque<>();
        for (int i = 0; i < 4; i++) {
            q.offer(new int[]{0, i});
            dp[0][i] = land[0][i];
        }

        while (!q.isEmpty()) {
            int[] rc = q.poll();
            for (int i = 0; i < 4; i++) {
                if (i == rc[1])
                    continue;
                int value = dp[rc[0]][rc[1]] + land[rc[0] + 1][i];
                if (value > dp[rc[0] + 1][i]) {
                    dp[rc[0] + 1][i] = value;
                    if (rc[0] + 1 < land.length - 1) {
                        q.offer(new int[] {rc[0] + 1, i});
                    }
                }
            }
        }
    }


    int solution(int[][] l) {
        land = new int[l.length+1][4];
        for (int r = 0; r < l.length; r++)
            for (int c = 0; c < 4; c++)
                land[r][c] = l[r][c];

        dp = new int[l.length+1][4];

//        for (int i = 0; i < 4; i++) {
//            dp[0][i] = land[0][i];
//            backtracking(1, i);
//        }
        bfs();

        int answer = 0;
        for (int i = 0; i < 4; i++)
            answer = Math.max(dp[l.length-1][i], answer);

        return answer;
    }
}









