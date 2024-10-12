import java.io.*;
import java.net.Inet4Address;
import java.util.*;

public class Main {
    static int N, M, K, X;
    static ArrayList<Integer>[] graph;
    static int[] weight;

    static ArrayList<Integer> answer;

    static void bfs() {
        Queue<Integer> q = new ArrayDeque<>();
        q.add(X);
        weight[X] = 0;

        while (!q.isEmpty()) {
            int curNode = q.poll();
            for (int nextNode : graph[curNode]) {
                if (weight[nextNode] == 1_000_001) {
                    weight[nextNode] = weight[curNode] + 1;
                    q.add(nextNode);
                    if (weight[nextNode] == K)
                        answer.add(nextNode);
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        N = read();
        M = read();
        K = read();
        X = read();
        graph = new ArrayList[N + 1];
        for (int i = 0; i < N + 1; i++)
            graph[i] = new ArrayList<>();
        weight = new int[N + 1];
        Arrays.fill(weight, 1_000_001);
        answer = new ArrayList<>();

        for (int i = 0; i < M; i++)
            graph[read()].add(read());

        bfs();

        StringBuilder sb = new StringBuilder();
        if (!answer.isEmpty()) {
            Collections.sort(answer);
            for (int node : answer)
                sb.append(node).append('\n');
            sb.deleteCharAt(sb.length() - 1);
            System.out.println(sb.toString());
        }
        else
            System.out.println(-1);

    }

    private static int read() throws Exception {
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32) {
            n = (n << 3) + (n << 1) + (c & 15);
        }
        return n;
    }
}