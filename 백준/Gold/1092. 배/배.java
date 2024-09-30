import java.io.*;
import java.util.*;
import java.util.stream.Stream;

// 234
public class Main {
    static int N, M, answer;
    static Integer[] crain;
    static Integer[] boxWeight;
    static int[] crainBoxIdx;
    static boolean[] visit;

    static int paramatricSearch(int idx) {
        int l = 0;
        int r = M-1;
        int answer = -1;
        while (l <= r) {
            int mid = (l + r)/2;
            if (crain[idx] >= boxWeight[mid]) {
                l = mid + 1;
                answer = mid;
            }
            else
                r = mid - 1;
        }
        return answer;
    }

    static void check() {
        answer = 0;
        while (true){
            boolean flag = false;
            for (int cIdx = 0; cIdx < N; cIdx++) {
                for (int i = crainBoxIdx[cIdx]; i >= 0; i--) {
                    if (visit[i])
                        continue;
                    if (crain[cIdx] >= boxWeight[i]) {
                        flag = visit[i] = true;
                        crainBoxIdx[cIdx] = i;
                        break;
                    }
                }
            }
            if (!flag)
                break;
            else
                answer++;
        }
    }
    public static void main(String[] args) throws Exception {
        N = read();
        crain = new Integer[N];
        for (int i = 0; i < N; i++)
            crain[i] = read();

        M = read();
        boxWeight = new Integer[M];
        visit = new boolean[M];

        for (int i = 0; i < M; i++) {
            boxWeight[i] = read();
        }

        Arrays.sort(boxWeight);

        crainBoxIdx = new int[N];
        for (int i = 0; i < N; i++) {
            crainBoxIdx[i] = paramatricSearch(i);
        }

        check();

        for (int i = 0; i < M; i++) {
            if (!visit[i]) {
                System.out.println(-1);
                return;
            }
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