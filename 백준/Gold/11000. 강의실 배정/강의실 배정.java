import java.io.*;
import java.util.*;

// 150
public class Main {
    static int N, answer;
    static int[][] schedules;
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        schedules = new int[N][2];

        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(bf.readLine());
            schedules[i][0] = Integer.parseInt(st.nextToken());
            schedules[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(schedules, ((o1, o2) -> {
            if (o1[0] - o2[0] != 0) {
                return o1[0] - o2[0];
            }
            else
                return o1[1] - o2[1];
        } ) );
        answer = 0;

        PriorityQueue<Integer> q = new PriorityQueue<>(((o1, o2) -> o1 - o2));
        for (int i = 0; i < N; i++) {
            // 큐의 맨 첫값이 현재 시작시간보다 이를 때
            if (!q.isEmpty() && q.peek() <= schedules[i][0])
                q.poll();
            else
                answer++;

            q.offer(schedules[i][1]);
        }

        System.out.println(answer);
    }
}