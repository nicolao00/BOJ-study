//753

import java.util.*;
import java.io.*;

class Main {
    static int V;
    static int E;
    static int start;
    static ArrayList<Map<Integer, Integer>> graph;
    static int[] dist;
    static PriorityQueue<int[]> pq;

    public static void dijkstra() {
        for (Map.Entry<Integer, Integer> tmp : graph.get(start).entrySet()) {
            dist[tmp.getKey()] = tmp.getValue();
            pq.offer(new int[]{tmp.getKey(), tmp.getValue()});
        }

        while(!pq.isEmpty()) {
            int[] map = pq.poll();
            int node = map[0];
            int d = map[1];

            for (Map.Entry<Integer, Integer> tmp : graph.get(node).entrySet()) {
                int nextNode = tmp.getKey();
                int sumDist = tmp.getValue() + d;
                if (sumDist < dist[nextNode]) {
                    dist[nextNode] = sumDist;
                    pq.offer(new int[]{nextNode, sumDist});
                }
            }
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        start = Integer.parseInt(bf.readLine());
        pq = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);

        graph = new ArrayList<>();
        for (int i = 0; i <= V; i++)
            graph.add(new HashMap<>());

        dist = new int[V + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(bf.readLine());
            int u = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            graph.get(u).put(w, Math.min(graph.get(u).getOrDefault(w, Integer.MAX_VALUE), d));
        }

        dijkstra();

        for (int i = 1; i <= V; i++) {
            if (dist[i] != Integer.MAX_VALUE)
                System.out.println(dist[i]);
            else
                System.out.println("INF");
        }
    }
}