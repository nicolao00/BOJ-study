import java.io.*;
import java.util.*;

// 424
public class Main {
    static int N, D, answer;
    static ArrayList<Rode> fast;

    static class Rode {
        int start;
        int end;
        int time;

        Rode(int start, int end, int time) {
            this.start = start;
            this.end = end;
            this.time = time;
        }
    }

    static void dfs(int start, int time, int idx) {
        if (answer <= time)
            return;
        if (start >= D) {
            answer = Math.min(answer, time);
            return;
        }
        if (idx > N - 1) {
            time += (D - start);
            answer = Math.min(answer, time);
            return;
        }

        // 지름길 가는거
        int nextIdx = idx;
        // 현재 위치보다 더 먼 시작위치의 지름길 찾기
        while (nextIdx <= N - 1 && (start > fast.get(nextIdx).start || fast.get(nextIdx).end > D)) {
            nextIdx++;
        }
        // 지름길 다 돌았을떄
        if (nextIdx > N - 1) {
            time += (D - start);
            answer = Math.min(answer, time);
            return;
        }
        dfs(fast.get(nextIdx).end, time + (fast.get(nextIdx).start - start) + fast.get(nextIdx).time, nextIdx+1);


        // 안가는거
        dfs(start, time, nextIdx + 1);
    }

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());
        fast = new ArrayList<>();

        for (int i = 0; i < N; i++) {

            st = new StringTokenizer(bf.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int time = Integer.parseInt(st.nextToken());

            fast.add(new Rode(start, end, time));
        }
        fast.sort(Comparator.comparingInt(o -> o.start));

        answer = D;
        dfs(0, 0, 0);
        System.out.println(answer);
    }
}
