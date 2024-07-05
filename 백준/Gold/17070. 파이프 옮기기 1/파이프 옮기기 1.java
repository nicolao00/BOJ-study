// 135 / 153
import java.util.*;
import java.io.*;

class Main {
    static int N;
    static int[][] board;
    // [놓인 상태(가로,세,대)][인덱스]
    static int[][] dr = new int[][]{
            {0, 1},
            {1, 1},
            {0, 1, 1}
    };
    static int[][] dc = new int[][]{
            {1, 1},
            {0, 1},
            {1, 0, 1}
    };
    static int[][] ds = new int[][]{
            {0, 2},
            {1, 2},
            {0, 1, 2}
    };

    public static void bfs() {
        int answer = 0;

        Queue<int[]> q = new ArrayDeque<>();
        // 놓인 상태S, R, C
        q.offer(new int[]{0, 1, 0});
        while(!q.isEmpty()) {
            int[] rcs = q.poll();
            int r = rcs[0];
            int c = rcs[1];
            int s = rcs[2];

            for (int i = 0; i < dr[s].length; i++) {
                int nr = r + dr[s][i];
                int nc = c + dc[s][i];
                int ns = ds[s][i];

                if (0 <= nr && nr < N && 0 <= nc && nc < N && board[nr][nc] == 0) {
                    if (ns == 2 && (board[nr-1][nc] != 0 || board[nr][nc-1] != 0))
                        continue;
                    if (nr == N-1 && nc == N-1){
                        answer++;
                        continue;
                    }
                    q.offer(new int[]{nr, nc, ns});
                }
            }
        }

        System.out.println(answer);
    }

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(bf.readLine());
        board = new int[N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        if (board[N-1][N-1] == 1)
            System.out.println(0);
        else
            bfs();
    }
}