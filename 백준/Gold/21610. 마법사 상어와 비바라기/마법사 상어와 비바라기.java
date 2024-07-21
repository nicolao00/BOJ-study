// 556 - 608 / 623 - 707 / 851

import java.util.*;
import java.io.*;

class Main {
    static int N;
    static int M;
    static int[][] board;
    static int[] dr = new int[] {0, -1, -1, -1, 0, 1, 1, 1};
    static int[] dc = new int[] {-1, -1, 0, 1, 1, 1, 0, -1};
    static Set<Pair> cloud;
    static Set<Pair> movedCloud;

    static class Pair {
        int x;
        int y;

        Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        Pair(Pair a) {
            this.x = a.x;
            this.y = a.y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Pair pair = (Pair) o;
            return x == pair.x && y == pair.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }

    // 1~3번 과정
    public static void moveCloud(int d, int s) {
        for (Pair rc : cloud) {
            // 1번
            int[] newRC = new int[]{ rc.x + dr[d]*s, rc.y + dc[d]*s };
             for (int i = 0; i < 2; i++) {
                if (newRC[i] < 0) {
                    int result = Math.abs(newRC[i]) % N;
                    if (result > 0)
                        newRC[i] = N - result;
                    else
                        newRC[i] = result;
                }
                else if (newRC[i] >= N)
                    newRC[i] %= N;
            }
            // 2번
            board[newRC[0]][newRC[1]] += 1;
            movedCloud.add(new Pair(newRC[0], newRC[1]));
        }
        // 3번
        cloud.clear();
    }

    // 4번 과정
    public static void copyWater() {
        ArrayList<int[]> tmp = new ArrayList<>();
        for (Pair rc : movedCloud) {
            int cnt = 0;
            for (int i = 1; i < 8; i+=2){
                int nr = rc.x + dr[i];
                int nc = rc.y + dc[i];
                if (0 <= nr && nr < N && 0 <= nc && nc < N && board[nr][nc] > 0)
                    cnt++;
            }
            tmp.add(new int[]{rc.x, rc.y, board[rc.x][rc.y] + cnt});
        }

        for (int[] change : tmp)
            board[change[0]][change[1]] = change[2];
    }

    // 5번 과정
    public static void makeCloud() {
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++){
                Pair tmp = new Pair(r, c);
                if (movedCloud.contains(tmp) || board[r][c] < 2)
                    continue;
                board[r][c] -= 2;
                cloud.add(tmp);
            }
        }
    }

    public static void main(String[] args) throws IOException{

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][N];
        cloud = new HashSet<>();
        movedCloud = new HashSet<>();

        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(bf.readLine());
            for (int c = 0; c < N; c++) {
                board[r][c] = Integer.parseInt(st.nextToken());
            }
        }

        cloud.add(new Pair(N-1, 0));
        cloud.add(new Pair(N-1, 1));
        cloud.add(new Pair(N-2, 0));
        cloud.add(new Pair(N-2, 1));
        // 이동 시작
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(bf.readLine());
            int d = Integer.parseInt(st.nextToken()) - 1;
            int s = Integer.parseInt(st.nextToken());

            // 1,2,3번 과정
            moveCloud(d, s);
            // 4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
            copyWater();
            // 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
            makeCloud();
            movedCloud.clear();
        }

        int answer = 0;
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                answer += board[i][j];
        System.out.println(answer);
    }
}