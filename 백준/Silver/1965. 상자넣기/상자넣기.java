import java.io.*;
import java.util.StringTokenizer;

// 142
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        int[] dp = new int[1001];

        StringTokenizer st = new StringTokenizer(bf.readLine());
        int answer = 0;
        for (int i = 0; i < N; i++) {
            int v = Integer.parseInt(st.nextToken());
            int max = 0;
            for (int j = v-1; j >= 0; j--) {
                if (max < dp[j])
                    max = dp[j];
            }
            dp[v] = max + 1;
            if (answer < dp[v])
                answer = dp[v];
        }
        System.out.println(answer);
    }
}