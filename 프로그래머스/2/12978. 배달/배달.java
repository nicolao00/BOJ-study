// 221
import java.util.*;

class Solution {
    public int solution(int N, int[][] road, int K) {
        int answer = 0;
        int[] dist = new int[N+1];
        Arrays.fill(dist, 500001);
        dist[1] = 0;
        int[][] board = new int[N+1][N+1];
        
        for (int[] info : road) {
            if (board[info[0]][info[1]] > 0)
                board[info[0]][info[1]] = Math.min(board[info[0]][info[1]], info[2]);
            else
                board[info[0]][info[1]] = info[2];
            if (board[info[1]][info[0]] > 0)
                board[info[1]][info[0]] = Math.min(board[info[1]][info[0]], info[2]);
            else
                board[info[1]][info[0]] = info[2];
        }
        
        // Queue<int[]> q = new Queue<>();
        PriorityQueue<int[]> q = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);
        q.offer(new int[]{1,0});
        while (!q.isEmpty()) {
            int[] nd = q.poll();
            for (int i = 1; i <= N; i++){
                // 자기자신으로 이동하거나 갈 수 없는 방향이면 패스
                if (i == nd[0] || board[nd[0]][i] == 0) continue;
                
                int newDist = dist[nd[0]] + board[nd[0]][i];
                if (newDist > K || newDist > dist[i]) continue;
                dist[i] = newDist;
                q.offer(new int[]{i, newDist});
            }
        }
        
        for (int i = 1; i <= N; i++) {
            if (dist[i] <= K)
                answer++;
        }
        return answer;
    }
}