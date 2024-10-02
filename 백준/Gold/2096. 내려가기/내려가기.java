import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

// 40 / 721
public class Main {
    static int N;
    static int[][] stairs;
    static int[][] maxDP;
    static int[][] minDP;
    static ArrayList<Integer>[] adjacent;
    static int maxValue, minValue;

    static void bfs() {
        for (int i = 0; i < 3; i++) {
            minDP[0][i] = stairs[0][i];
            maxDP[0][i] = stairs[0][i];
        }

        for (int r = 0; r < N-1; r++) {
            for (int c = 0; c < 3; c++) {
                for (int nextIdx : adjacent[c]) {
                    maxDP[r + 1][nextIdx] = Math.max(maxDP[r + 1][nextIdx], maxDP[r][c] + stairs[r+1][nextIdx]);
                    minDP[r + 1][nextIdx] = Math.min(minDP[r + 1][nextIdx], minDP[r][c] + stairs[r+1][nextIdx]);
                }
            }
        }
    }
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        stairs = new int[N][3];
        maxDP = new int[N][3];
        minDP = new int[N][3];

        adjacent = new ArrayList[3];
        for (int i = 0; i < 3; i++)
            adjacent[i] = new ArrayList<>();
        adjacent[0].add(0); adjacent[0].add(1);
        adjacent[1].add(0); adjacent[1].add(1); adjacent[1].add(2);
        adjacent[2].add(1); adjacent[2].add(2);

        for (int i = 0; i < N; i++)
            Arrays.fill(minDP[i], 900001);

        for (int r = 0; r < N; r++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            stairs[r][0] = Integer.parseInt(st.nextToken());
            stairs[r][1] = Integer.parseInt(st.nextToken());
            stairs[r][2] = Integer.parseInt(st.nextToken());
        }

        bfs();
        int min = minDP[N-1][0];
        int max = maxDP[N-1][0];
        for (int i = 1; i < 3; i++) {
            min = Math.min(min, minDP[N - 1][i]);
            max = Math.max(max, maxDP[N - 1][i]);
        }

        System.out.println(max + " " + min);
    }
}