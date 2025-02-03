import java.util.*;
import java.io.*;

class Main {
    static int[] parents;
    public static void main(String[] args) throws Exception{
        int N = read();
        int M = read();
        parents = new int[N+1];
        for (int i = 1; i <= N; i++) {
            parents[i] = i;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < M; i++) {
            int a = read();
            int b = read();
            int c = read();

            if (a == 0) {
                union_root(b, c);
            } else {
                if (find_root(b) == find_root(c))
                    sb.append("YES").append('\n');
                else
                    sb.append("NO").append('\n');
            }
        }
        System.out.println(sb.toString());
    }

    public static int find_root(int x) {
        if (parents[x] == x)
            return x;
        parents[x] = find_root(parents[x]);
        return parents[x];
    }

    public static void union_root(int x, int y) {
        int X = find_root(x);
        int Y = find_root(y);
        if (X != Y) {
            parents[X] = parents[Y];
        }
    }

    // 걍 띄워쓰기 기준으로 다 하나씩 숫자 입력받는 듯?
    private static int read() throws Exception {
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32) {
            n = (n << 3) + (n << 1) + (c & 15);
        }
        return n;
    }
}