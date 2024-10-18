import java.io.*;
import java.util.*;

// 424
public class Main {
    static int[][] board;
    static int[][] dist;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    static int R, C;

    static class Point {
        int r;
        int c;

        Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    static void bfs(int sR, int sC) {
        Queue<Point> q = new ArrayDeque<>();
        q.offer(new Point(sR, sC));

        while (!q.isEmpty()) {
            Point p = q.poll();

            for (int i = 0; i < 4; i++) {
                int nr = p.r + dr[i];
                int nc = p.c + dc[i];

                if (0 <= nr && nr < R && 0 <= nc && nc < C && board[nr][nc] == 1 && dist[nr][nc] == 0) {
                    dist[nr][nc] = dist[p.r][p.c] + 1;
                    q.offer(new Point(nr, nc));
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        board = new int[R][C];
        dist = new int[R][C];

        int startR = 0;
        int startC = 0;
        for (int r = 0; r < R; r++) {
            st = new StringTokenizer(bf.readLine());
            for (int c = 0; c < C; c++) {
                board[r][c] = Integer.parseInt(st.nextToken());
                if (board[r][c] == 2) {
                    startR = r;
                    startC = c;
                }
            }
        }

        dist[startR][startC] = 0;
        board[startR][startC] = 0;
        bfs(startR, startC);

        StringBuilder sb = new StringBuilder();
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C-1; c++) {
                if (dist[r][c] == 0 && board[r][c] == 1)
                    sb.append(-1);
                else
                    sb.append(dist[r][c]);
                sb.append(' ');
            }
            if (dist[r][C-1] == 0 && board[r][C-1] == 1)
                sb.append(-1);
            else
                sb.append(dist[r][C-1]);
            if (r != R - 1)
                sb.append('\n');
        }
        System.out.println(sb.toString());
    }
}
