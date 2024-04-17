// 811
import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main{
    static class Pair {
        int node;
        int dist;
        public Pair(int n, int d){
            node = n;
            dist = d;
        }
    }

    public static void main(String args[]) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        // N: 헛간 개수  /  M: 길 개수
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 이웃한 노드 저장하는 리스트
        ArrayList<Integer>[] arr = new ArrayList[N+1];
        for (int i=0; i<=N; i++){
            arr[i] = new ArrayList<Integer>();
        }

        // 이웃한 노드 서로 저장
        for (int i=0; i<M; i++){
            st = new StringTokenizer(bf.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a].add(b); arr[b].add(a);
        }

        Deque<Pair> dq = new LinkedList<>();
        boolean[] visit = new boolean[N+1];
        // 시작점으로부터 거리를 저장할 배열
        int[] dist = new int[N+1];
        visit[0] = true; visit[1] = true;
        dq.offer(new Pair(1, 0));
        while (!dq.isEmpty()){
            Pair p = dq.poll();
            for (int nextN: arr[p.node]){
                if (!visit[nextN]){
                    visit[nextN] = true;
                    dist[nextN] = p.dist+1;
                    dq.offer(new Pair(nextN, p.dist+1));
                }
            }
        }

        int answer = 0;
        int distance = 0;
        int cnt = 0;
        for (int i = 1; i<N+1; i++){
            if (distance < dist[i]){
                distance = dist[i];
                answer = i;
                cnt = 1;
            }
            else if (distance == dist[i]){
                cnt++;
            }
        }

        System.out.println(Integer.toString(answer) + ' ' + Integer.toString(dist[answer]) + ' ' + Integer.toString(cnt));
    }
}