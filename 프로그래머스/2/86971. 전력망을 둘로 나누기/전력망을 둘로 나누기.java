// 835-958
import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = 999999;
        
        // 서로 연관된 타워를 저장
        ArrayList<Integer>[] tower = new ArrayList[n+1];
        for (int i = 0; i < n+1; i++) {
            tower[i] = new ArrayList<Integer>();
        }
        for (int i=0; i < wires.length; i++){
            tower[wires[i][0]].add(wires[i][1]);
            tower[wires[i][1]].add(wires[i][0]);
        }
        
        // 전선을 하나씩 끊어서 완전탐색
        for (int i=0; i < wires.length; i++){
            int[] result = new int[2];
            boolean[] visit = new boolean[n+1];
            
            int[] disconnect = new int[]{wires[i][0], wires[i][1]};
            visit[wires[i][0]] = true; visit[wires[i][1]] = true;
            
            for (int start = 0; start < 2; start++){
                Deque<Integer> dq = new LinkedList<>();
                dq.offer(disconnect[start]);
                
                while(!dq.isEmpty()){
                    int node = dq.poll();
                    for (int child: tower[node]){
                        if (!visit[child]){
                            dq.offer(child);
                            result[start]++;
                            visit[child] = true;
                        }
                    }
                }
            }
            answer = Math.min(answer, Math.abs(result[0] - result[1]));
        }
        return answer;
    }
}