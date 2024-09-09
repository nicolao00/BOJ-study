import java.io.*;
import java.util.*;

// 301
public class Main {
    static int eggCnt;
    static int[] life;
    static int[] weight;
    static int answer;

    public static void dfs(int cnt) {
        if (cnt == eggCnt) {
            int result = 0;
            for (int l : life) {
                if (l <= 0) {
                    result++;
                }
            }
            answer = Math.max(result, answer);
            return;
        }

        boolean hit = false;
        for (int i = 0; i < eggCnt; i++) {
            if (life[i] < 0 || life[cnt] < 0 || i == cnt) {
                continue;
            }
            hit = true;
            int tmp = weight[i];
            life[i] -= weight[cnt];
            life[cnt] -= tmp;
            dfs(cnt + 1);
            life[i] += weight[cnt];
            life[cnt] += tmp;
        }
        if (!hit)
            dfs(cnt + 1);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        eggCnt = Integer.parseInt(bf.readLine());
        life = new int[eggCnt];
        weight = new int[eggCnt];

        for (int i = 0; i < eggCnt; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            life[i] = Integer.parseInt(st.nextToken());
            weight[i] = Integer.parseInt(st.nextToken());
        }

        answer = 0;
        dfs(0);
        System.out.println(answer);
    }
}