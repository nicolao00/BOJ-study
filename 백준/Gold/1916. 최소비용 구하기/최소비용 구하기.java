import java.util.*;
import java.io.*;

// 227
class Main {
    static int N;
    static int M;
    static int[][] graph;
    static boolean[] visit;
    static int[] distince;
    static int start;
    static int goal;

    public static void djick() {
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[0] - o2[0]);
        pq.add(new int[]{0, start});
        visit[0] = true;

        while (!pq.isEmpty()) {
            int[] node = pq.poll();
            int cost = node[0];
            int nIdx = node[1];

            for (int i = 1; i <= N; i++) {
                if (graph[nIdx][i] == 100_001)
                    continue;
                if (cost + graph[nIdx][i] < distince[i]) {
                    distince[i] = cost + graph[nIdx][i];
                    if (i != goal) {
                        pq.offer(new int[]{distince[i], i});
                        visit[i] = true;
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        M = Integer.parseInt(bf.readLine());
        graph = new int[N+1][N+1];
        distince = new int[N + 1];
        visit = new boolean[N + 1];
        Arrays.fill(distince, 100_000_001);
        for (int i = 0; i <= N; i++)
            Arrays.fill(graph[i], 100_001);


        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int start = Integer.parseInt(st.nextToken());
            int dest = Integer.parseInt(st.nextToken());
            graph[start][dest] = Math.min(graph[start][dest], Integer.parseInt(st.nextToken()));
        }

        StringTokenizer st = new StringTokenizer(bf.readLine());
        start = Integer.parseInt(st.nextToken());
        goal = Integer.parseInt(st.nextToken());
        distince[start] = 0;

        djick();
        System.out.println(distince[goal]);
    }
}
