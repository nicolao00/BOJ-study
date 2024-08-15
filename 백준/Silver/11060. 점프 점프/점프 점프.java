import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

// 142
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        int[] dp = new int[N+1];
        Arrays.fill(dp, 1001);
        dp[1] = 0;
        int[] arr = new int[N + 1];

        StringTokenizer st = new StringTokenizer(bf.readLine());
        for (int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            for (int t = i+1; t <= Math.min(i + arr[i], N); t++) {
                if (dp[t] > dp[i] + 1)
                    dp[t] = dp[i] + 1;
            }
        }
        if (dp[N] != 1001)
            System.out.println(dp[N]);
        else
            System.out.println(-1);
    }
}