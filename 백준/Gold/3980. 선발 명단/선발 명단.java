import java.io.*;
import java.util.*;

// 301
public class Main {
    static int[][] stat;
    static boolean[] visit;
    static int answer;

    public static void makePer(int position, int result) {
        if (position == 11){
            answer = Math.max(result, answer);
            return;
        }

        for (int player = 0; player < 11; player++) {
            if (visit[player] || stat[player][position] == 0)
                continue;
            visit[player] = true;
            makePer(position + 1, result + stat[player][position]);
            visit[player] = false;
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int testCase = Integer.parseInt(bf.readLine());
        StringBuilder sb = new StringBuilder();

        for (int tIdx = 0; tIdx < testCase; tIdx++) {
            stat = new int[11][11];

            for (int i = 0; i < 11; i++) {
                StringTokenizer st = new StringTokenizer(bf.readLine());
                for (int j = 0; j < 11; j++)
                    stat[i][j] = Integer.parseInt(st.nextToken());
            }

            answer = 0;
            visit = new boolean[11];
            makePer(0, 0);
            sb.append(answer).append('\n');
        }
        sb.deleteCharAt(sb.length() - 1);
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}