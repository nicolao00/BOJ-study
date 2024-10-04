import java.io.*;
import java.util.*;

// 203
public class Main {
    static int N, M;
    static int[][] board;
    static boolean[][] visit;
    static int[][] dr = {
            {0, 0, 1},
            {0, 0, -1},
            {-1, 0, 0},
            {1, 0, 0}
    };
    static int[][] dc = {
            {-1, 0, 0},
            {-1, 0, 0},
            {0, 0, 1},
            {0, 0, 1}
    };
    static int answer;

    static boolean check(int r, int c, int dirIdx) {

        return true;
    }

//    static void dfs(int row, int col, int value) {
//        for (int r = row; r < N; r++) {
//            for (int c = 0; c < M; c++) {
//                if (visit[r][c])
//                    continue;
//
//                for (int dirIdx = 0; dirIdx < 4; dirIdx++) {
//                    newValue = value;
//                    if (check(r, c, dirIdx)) {
//                        dfs(row, col, value + board[r][c]);
//                    }
//                }
//            }
//        }
//        answer = Math.max(answer, );
//    }

    static void dfs(int r, int c, int value) {
        if (c > M - 1) {
            r++;
            c = 0;
        }

        if (r > N - 1) {
            answer = Math.max(answer, value);
            return;
        }

        if (visit[r][c]) {
            dfs(r, c+1, value);
            return;
        }

        // 네가지 모양 모두 탐색
        ArrayList<int[]> rcList = new ArrayList<>();
        for (int dirIdx = 0; dirIdx < 4; dirIdx++) {
            // 각 모양에서 사용할 값
            int newValue = value;

            boolean flag = true;
            for (int i = 0; i < 3; i++) {
                int nr = r + dr[dirIdx][i];
                int nc = c + dc[dirIdx][i];

                if (0 <= nr && nr < N && 0 <= nc && nc < M && !visit[nr][nc]) {
                    visit[nr][nc] = true;
                    rcList.add(new int[]{nr, nc});
                    newValue += board[nr][nc];
                } else {
                    flag = false;
                    break;
                }
            }
            // 해당 모양으로 사용가능하면
            if (flag) {
                dfs(r, c+1, newValue + board[r][c]);
            }
            for (int[] rc : rcList) {
                visit[rc[0]][rc[1]] = false;
            }
        }
        dfs(r, c+1, value);
    }

    public static void main(String[] args) throws Exception {
        N = read();
        M = read();
        board = new int[N][M];
        visit = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                board[i][j] = read();
            }
        }

        answer = 0;
        dfs(0, 0, 0);
        System.out.println(answer);
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

//2 3
//        7 5 4
//        3 2 9