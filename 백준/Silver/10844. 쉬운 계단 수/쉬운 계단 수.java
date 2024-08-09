import java.io.*;

class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        long [][] dp = new long[N+1][10];
        dp[0][1] = 1;
        for (int i = 1; i <= 9; i++)
            dp[1][i] = 1;


        for (int i = 2; i <= N; i++) {
            dp[i][1] = ((dp[i-2][1] % 1000000000) + (dp[i-1][2] % 1000000000)) % 1000000000;
            for (int j = 2; j <= 8; j++) {
                dp[i][j] = ((dp[i-1][j-1] % 1000000000) + (dp[i-1][j+1] % 1000000000)) % 1000000000;
            }
            dp[i][9] = dp[i-1][8];
        }
        long answer = 0;
        for (int i = 1; i <= 9; i++) {
            answer = ((answer % 1000000000) + (dp[N][i] % 1000000000)) % 1000000000;
        }
        System.out.println(answer);
    }
}