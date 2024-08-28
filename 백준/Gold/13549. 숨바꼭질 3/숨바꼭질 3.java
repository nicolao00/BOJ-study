import java.io.*;
import java.util.*;

//107
public class Main {
    static int N, K;
    static int[] dp;
    static int answer;

    public static void bfs() {
        PriorityQueue<int[]> q = new PriorityQueue<>((o1, o2) -> (o1[0] - o2[0]));
        q.offer(new int[]{0, N});
        dp[N] = 0;

        while (!q.isEmpty()) {
            int[] distNum = q.poll();
            if (answer <= distNum[0])
                continue;

            // 순간이동
            int i = distNum[1]*2;
            if (i < 200000) {
                if (i == K) {
                    answer = Math.min(distNum[0], answer);
                    return;
                }
                if (distNum[0] < dp[i]) {
                    dp[i] = distNum[0];
                    q.offer(new int[]{distNum[0], i});
                }
            }
            // + 1로 이동
            if (distNum[1] + 1 < dp.length && distNum[0] + 1 < dp[distNum[1] + 1]) {
                if (distNum[1] + 1 == K) {
                    answer = Math.min(distNum[0] + 1, answer);
                    continue;
                }
                dp[distNum[1] + 1] = distNum[0] + 1;
                q.offer(new int[]{distNum[0] + 1, distNum[1] + 1});
            }
            // -1로 이동
            if (distNum[1] - 1 >= 0 && distNum[0] + 1 < dp[distNum[1] - 1]) {
                if (distNum[1] - 1 == K) {
                    answer = Math.min(distNum[0] + 1, answer);
                    continue;
                }
                dp[distNum[1] + 1] = distNum[0] + 1;
                q.offer(new int[]{distNum[0] + 1, distNum[1] - 1});
            }
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        dp = new int[200001];
        answer = 100001;
        Arrays.fill(dp, 100001);
        dp[N] = 0;

        if (N != K) {
            bfs();
            System.out.println(answer);
        }
        else
            System.out.println(0);

    }
}
//3 6 12 11 22