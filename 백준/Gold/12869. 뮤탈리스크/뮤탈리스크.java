import java.util.*;
import java.io.*;

// 552 - 700 / 1219
class Main {
    static int N;
    static int[] scvs;
    static int[][][] dp = new int[61][61][61];
    static int answer = Integer.MAX_VALUE;
    static int[][] comb3 = new int[][] {
            {-9, -3, -1},
            {-9, -1, -3},
            {-3, -9, -1},
            {-3, -1, -9},
            {-1, -9, -3},
            {-1, -3, -9},
    };

    public static void bfs(int[] energe, int cnt) {
        if (cnt >= answer)
            return;
        if (dp[energe[0]][energe[1]][energe[2]] != 0 && dp[energe[0]][energe[1]][energe[2]] <= cnt)
            return;

        dp[energe[0]][energe[1]][energe[2]] = cnt;

        if (energe[0] == 0 && energe[1] == 0 && energe[2] == 0){
            answer = Math.min(cnt, answer);
            return;
        }

        for (int i = 0; i < comb3.length; i++) {
            bfs(new int[] {Math.max(energe[0] + comb3[i][0], 0), Math.max(energe[1] + comb3[i][1],0), Math.max(energe[2] + comb3[i][2], 0)}, cnt + 1);
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        scvs = new int[3];

        StringTokenizer st = new StringTokenizer(bf.readLine());
        for (int i = 0; i < N; i++)
            scvs[i] = Integer.parseInt(st.nextToken());

        bfs(scvs, 0);

        System.out.println(answer);
    }
}