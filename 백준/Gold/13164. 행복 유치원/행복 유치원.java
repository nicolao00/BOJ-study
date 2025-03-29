import java.io.*;
import java.util.*; 

public class Main {
    static int N, K;
    static int[] heights;
    static int[] diffs;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        heights = new int[N];
        diffs = new int[N];
        int answer = 0;

        st = new StringTokenizer(bf.readLine());
        heights[0] = Integer.parseInt(st.nextToken());
        for (int i = 1; i < N; i++) {
            heights[i] = Integer.parseInt(st.nextToken());
            diffs[i] = heights[i] - heights[i-1];
        }
        Arrays.sort(diffs);
        for (int i = 0; i < N - K + 1; i++) {
            answer += diffs[i];
        }
        System.out.println(answer);
    }
}