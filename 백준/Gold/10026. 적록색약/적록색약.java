// 920
import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main{
    static int N;
    static char[][] board;
    static boolean[][][] visit;
    static boolean[][] sVisit;
    static RC[] drdc;

    public static class RC {
        int r;
        int c;
        public RC(int r, int c){
            this.r = r;
            this.c = c;
        }
    }

    public static void bfs(int r, int c) {
        Deque<RC> dq = new LinkedList<>();
        dq.offer(new RC(r, c));
        while (!dq.isEmpty()) {
            RC rc1 = dq.poll();
            for (RC rc2 : drdc) {
                int nr = rc1.r + rc2.r;
                int nc = rc1.c + rc2.c;
                if (0 <= nr && nr < N && 0 <= nc && nc < N && !visit[0][nr][nc]){
                    if (board[rc1.r][rc1.c] == board[nr][nc]){
                        dq.offer(new RC(nr, nc));
                        visit[0][nr][nc] = true;
                    }
                }
            }
        }
    }

    public static void sBfs(int r, int c) {
        Deque<RC> dq = new LinkedList<>();
        dq.offer(new RC(r, c));
        while (!dq.isEmpty()) {
            RC rc1 = dq.poll();
            for (RC rc2 : drdc) {
                int nr = rc1.r + rc2.r;
                int nc = rc1.c + rc2.c;
                if (0 <= nr && nr < N && 0 <= nc && nc < N && !visit[1][nr][nc]){
                    if ((board[rc1.r][rc1.c] == board[nr][nc]) || (board[rc1.r][rc1.c] != 'B' && board[nr][nc] != 'B')){
                        dq.offer(new RC(nr, nc));
                        visit[1][nr][nc] = true;
                    }
                }
            }
        }
    }

    public static void main(String args[]) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        // N: 맵의 크기
        N = Integer.parseInt(bf.readLine());
        board = new char[N][N];
        visit = new boolean[][][]{
                new boolean[N][N],
                new boolean[N][N]
        };
        drdc = new RC[]{
                new RC(-1, 0),
                new RC(0, 1),
                new RC(1, 0),
                new RC(0, -1),
        };
        int[] group = {0, 0};

        for (int i = 0; i < N; i++)
            board[i] = bf.readLine().toCharArray();

        for (int pIdx = 0; pIdx < 2; pIdx++){
            group[pIdx] = 0;
            for (int i = 0; i < N; i++){
                for (int j = 0; j < N; j++){
                    if (!visit[pIdx][i][j]){
                        visit[pIdx][i][j] = true;
                        if (pIdx == 0)
                            bfs(i, j);
                        else
                            sBfs(i, j);
                        group[pIdx]++;
                    }
                }
            }
        }
        System.out.println(Integer.toString(group[0]) + ' ' + Integer.toString(group[1]));
    }
}