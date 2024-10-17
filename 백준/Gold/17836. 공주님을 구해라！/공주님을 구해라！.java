import java.io.*;
import java.util.*;

// 424
public class Main {
    static int[][] board;
    static boolean[][] visit;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};
    static int answer;
    static boolean flag;

    static int R, C, T;
    static void bfs() {
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{0, 0, 0});
        visit[0][0] = true;

        while (!q.isEmpty()) {
            int[] rcd = q.poll();
            // 백트래킹 느낌
            if (rcd[2] > answer)
                continue;

            for (int i = 0; i < 4; i++) {
                int nr = rcd[0] + dr[i];
                int nc = rcd[1] + dc[i];

                if (0 <= nr && nr < R && 0 <= nc && nc < C && !visit[nr][nc] && board[nr][nc] != 1) {
                    visit[nr][nc] = true;
                    if (board[nr][nc] == 2) {
                        int result = rcd[2] + 1 + (R-1 - nr + C-1 - nc);
                        if (result <= answer) {
                            answer = result;
                            flag = true;
                        }
                    } else if (nr == R - 1 && nc == C - 1) {
                        int result = rcd[2] + 1;
                        if (result <= answer) {
                            answer = result;
                            flag = true;
                            return;
                        }
                    } else {
                        q.offer(new int[]{nr, nc, rcd[2] + 1});
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());
        board = new int[R][C];
        visit = new boolean[R][C];
        flag = false;

        for (int r = 0; r < R; r++) {
            st = new StringTokenizer(bf.readLine());
            for (int c = 0; c < C; c++) {
                board[r][c] = Integer.parseInt(st.nextToken());
            }
        }

        answer = T;
        bfs();

        if (answer <= T && flag)
            System.out.println(answer);
        else
            System.out.println("Fail");
    }
}
