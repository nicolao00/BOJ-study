import java.io.*;
import java.util.*;

// 2238 - 316
public class Main {
    static int N;
    static int[][] board;
    static int[] dr = new int[]{-1, 0, 1, 0};
    static int[] dc = new int[]{0, 1, 0, -1};
    static boolean[][] visit;
    static int answer;

    public static void dfs(int cnt, int number, int value) {
        if (value >= answer)
            return;
        if (cnt == 3) {
            answer = value;
            return;
        }

        for (int num = number; num < N * N; num++) {
            int r = num / N;
            int c = num % N;
            boolean flag = true;
            int newValue = value + board[r][c];

            if (visit[r][c])
                continue;
            visit[r][c] = true;
            ArrayList<Integer> flower = new ArrayList<>();
            flower.add(num);
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                if (0 <= nr && nr < N && 0 <= nc && nc < N && !visit[nr][nc]) {
                    newValue += board[nr][nc];
                    visit[nr][nc] = true;
                    flower.add(nr * N + nc);
                } else {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                dfs(cnt + 1, number + 1, newValue);
            }
            for (int flowerNum : flower) {
                int nr = flowerNum / N;
                int nc = flowerNum % N;
                visit[nr][nc] = false;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());

        board = new int[N][N];
        visit = new boolean[N][N];
        answer = 1000000;
        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(bf.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dfs(0, N+1, 0);
        if (answer == 1000000) {
            System.out.println(0);
        }
        else
            System.out.println(answer);
    }
}
