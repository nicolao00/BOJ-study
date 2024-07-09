// 655 - 710
import java.util.*;
import java.io.*;

class Main {
    // 배열의 크기
    static int n;
    // 일한 횟수
    static int m;
    // 배열
    static int[] arr;
    static int sIdx;
    static int eIdx;
    static int k;

    public static void routine() {
        int[] nArr = new int[eIdx - sIdx + 1];

        for (int i = sIdx; i <= eIdx; i++)
            nArr[i-sIdx] = arr[i];
        Arrays.sort(nArr);
        System.out.println(nArr[k]);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n];

        st = new StringTokenizer(bf.readLine());
        for (int i = 0; i < n; i++)
            arr[i] = Integer.parseInt(st.nextToken());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(bf.readLine());
            sIdx = Integer.parseInt(st.nextToken()) - 1;
            eIdx = Integer.parseInt(st.nextToken()) - 1;
            k = Integer.parseInt(st.nextToken()) - 1;

            routine();
        }
    }
}