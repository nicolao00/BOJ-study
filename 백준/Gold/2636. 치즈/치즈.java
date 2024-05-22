// 901
import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main{
    static int R, C;
    static Queue<RC> deleteCZ;
    static int[][] board;
    static boolean[][] visit;
    static boolean[][] visitAir;
    static int time;
    static int exAnswer;
    static int answer;
    static RC[] drdc;

    public static class RC {
        int r;
        int c;
        public RC(int r, int c){
            this.r = r;
            this.c = c;
        }
    }

    public static void bfs(int row, int col) {
        Queue<RC> q = new LinkedList<RC>();
        q.offer(new RC(row, col));

        while (!q.isEmpty()){
            RC rc = q.poll();
            for (int i = 0; i < 4; i++){
                int nr = rc.r + drdc[i].r;
                int nc = rc.c + drdc[i].c;

                if (0 <= nr && nr < R && 0 <= nc && nc < C && !visit[nr][nc]) {
                    if (board[nr][nc] == 0){
                        q.offer(new RC(nr, nc));
                    }
                    else {
                        deleteCZ.offer(new RC(nr, nc));
                        answer--;
                    }
                    visit[nr][nc] = true;
                }
            }
        }
    }

    public static void main(String args[]) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        // N: 세로
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        board = new int[R][C];
        visit = new boolean[R][C];
        drdc = new RC[]{
                new RC(-1, 0),
                new RC(0, 1),
                new RC(1, 0),
                new RC(0, -1),
        };

        for (int i = 0; i < R; i++){
            st = new StringTokenizer(bf.readLine());
            for (int j = 0; j < C; j++){
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] == 1)
                    answer++;
            }
        }

        while (answer > 0){
            time++;
            exAnswer = answer;
            deleteCZ = new LinkedList<RC>();

            visit = new boolean[R][C];
            visit[0][0] = true;
            bfs(0,0);

            while (!deleteCZ.isEmpty()){
                RC rc = deleteCZ.poll();
                board[rc.r][rc.c] = 0;
            }
        }

        System.out.println(time);
        System.out.println(exAnswer);
    }
}