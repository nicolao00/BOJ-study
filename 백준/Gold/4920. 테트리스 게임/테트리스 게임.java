import java.util.*;
import java.io.*;


// 832
class Main {
    static int N;
    static int[][] board;
    static int[][] puzzleR = {
            // 1번 퍼즐
            {0, 0, 0, 0},
            {0, 1, 2, 3},

            // 2
            {0, 0, 1, 1},
            {0, 1, 1, 2},

            // 3
            {0, 0, 0, 1},
            {0, 1, 2, 2},
            {0, 1, 1, 1},
            {0, 0, 1, 2},

            // 4
            {0, 0, 1, 0},
            {0, 1, 1, 2},
            {0, 1, 1, 1},
            {0, 0, -1, 1},

            // 5
            {0, 0, 1, 1}
    };
    static int[][] puzzleC = {
            // 1번 퍼즐
            {0, 1, 2, 3},
            {0, 0, 0, 0},

            {0, 1, 1, 2},
            {0, 0, -1, -1},

            {0, 1, 2, 2},
            {0, 0, 0, -1},
            {0, 0, 1, 2},
            {0, 1, 0, 0},

            {0, 1, 1, 2},
            {0, 0, 1, 0},
            {0, 0, -1, 1},
            {0, 1, 1, 1},

            {0, 1, 0, 1}
    };

    public static int simulate() {
        int answer = -6000000;
        for (int i = 0; i < 13; i++) {
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < N; c++) {
                    int result = 0;
                    boolean flag = true;
                    for (int idx = 0; idx < 4; idx++) {
                        int nr = r + puzzleR[i][idx];
                        int nc = c + puzzleC[i][idx];
                        if ((0 <= nr && nr < N) && (0 <= nc && nc < N)) {
                            result += board[nr][nc];
                        } else {
                            flag = false;
                        }
                    }
                    if (flag)
                        answer = Math.max(answer, result);
                }
            }
        }
        return answer;
    }

    public static void main(String[] args) throws Exception{
        StringBuilder sb = new StringBuilder();
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int testIdx = 0;
        while (true) {
            N = Integer.parseInt(bf.readLine().trim());
            if (N == 0)
                break;

            board = new int[N][N];
            for (int r = 0; r < N; r++) {
                StringTokenizer st = new StringTokenizer(bf.readLine().trim());
                for (int c = 0; c < N; c++) {
                    board[r][c] = Integer.parseInt(st.nextToken());
                }
            }

            int ans = simulate();
            testIdx++;
            sb.append(testIdx).append('.').append(' ').append(ans).append('\n');
        }
        sb.deleteCharAt(sb.length() - 1);
        System.out.println(sb.toString());
    }
}