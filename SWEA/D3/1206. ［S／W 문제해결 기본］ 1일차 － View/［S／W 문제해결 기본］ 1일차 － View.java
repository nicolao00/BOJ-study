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
            ArrayList<Integer> heights = new ArrayList<>();

            for (int i = 0; i < N; i++) {
                int a = Integer.parseInt(st.nextToken());
                heights.add(a);
            }

            int answer = 0;
            for (int i = 2; i < N-2; i++) {
                int h = heights.get(i);
                int temp = 999;
                for (int j = -2; j < 3; j++) {
                    if (j == 0) continue;
                    temp = Math.min(temp, h - heights.get(i + j));
                }
                if (0 < temp && temp != 999) answer += temp;
            }
            sb.append('#').append(test).append(' ').append(answer);
            System.out.println(sb);
            sb.setLength(0);
        }
    }
}
