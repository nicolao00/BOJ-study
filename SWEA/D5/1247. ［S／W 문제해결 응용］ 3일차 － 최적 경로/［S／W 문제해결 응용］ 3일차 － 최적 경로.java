import java.awt.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

// 1149
class Solution {
    static int N;
    static int answer;
    static Point company;
    static Point home;
    static Point[] points;
    static boolean[] visited;

    static public int distance(Point a, Point b) {
        return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
    }

    static public void dfs(int cnt, Point p, int weight) {
        if (cnt == N) { // 고객 집 다 돌았을 때
            answer = Math.min(answer, weight + distance(p, home));
            return;
        }
        else if (weight > answer) { // 백트래킹
            return;
        }

        for (int i = 0; i < N; i++){
            if (!visited[i]){
                visited[i] = true;
                dfs(cnt + 1, points[i], weight + distance(p, points[i]));
                visited[i] = false;
            }
        }
        return;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int testCase = Integer.parseInt(br.readLine());
        for (int test = 1; test <= testCase; test++) {
            answer = 9999999;
            N = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());

            company = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            home = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            points = new Point[N];
            visited = new boolean[N];
            for (int i = 0; i < N; i++)
                points[i] = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));

            dfs(0, company, 0);

            sb.append('#').append(test).append(' ').append(answer);
            System.out.println(sb);
            sb.setLength(0);
        }
    }
}
