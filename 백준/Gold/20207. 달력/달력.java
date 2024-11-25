// 1106
import java.util.*;
import java.io.*;

class Main {
    static boolean[] isExistSch;
    static int[] scheduleCnt;
    static int N;

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        isExistSch = new boolean[366];
        scheduleCnt = new int[366];

        int min = 1;
        int max = 365;
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            for (int s = start; s <= end; s++) {
                scheduleCnt[s]++;
                isExistSch[s] = true;
            }
            min = Math.min(start, min);
            max = Math.max(end, max);
        }

        int answer = 0;
        int i = min;
        int width = 0;
        int height = 0;
        while (i <= max) {
            width = height = 0;
            while (i <= max && isExistSch[i]) {
                width++;
                if (scheduleCnt[i] > height)
                    height = scheduleCnt[i];
                i++;
            }
            answer += width * height;
            i++;
        }
        System.out.println(answer);
    }
    private static int read() throws Exception {
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32) {
            n = (n << 3) + (n << 1) + (c & 15);
        }
        return n;
    }
}