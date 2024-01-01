import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        for (int test = 1; test < 11; test++) {
            int N = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] heights = new int[N];

            for (int i = 0; i < N; i++)
                heights[i] = Integer.parseInt(st.nextToken());

            int answer = 0;
            for (int i = 2; i < N-2; i++) {
                int h = heights[i];
                int temp = 0;
                for (int j = -2; j < 3; j++) {
                    if (j == 0) continue;
                    temp = Math.max(temp, heights[i - j]);
                }
                answer += Math.max(0, h - temp);
            }
            sb.append('#').append(test).append(' ').append(answer);
            System.out.println(sb);
            sb.setLength(0);
        }
    }
}
