import java.io.*;
import java.util.*;

// 141
public class Main {
    static int N;
    static int[] start, goal;

    static void check() {
        int[] arr = new int[N];
        for (int i = 0; i < N; i++)
            arr[i] = start[i];

        int answer = 0;
        for (int i = 1; i < N; i++) {
            if (arr[i-1] != goal[i-1]) {
                arr[i-1] = (arr[i-1] + 1) % 2;
                arr[i] = (arr[i] + 1) % 2;
                if (i != N-1)
                    arr[i+1] = (arr[i+1] + 1) % 2;
                answer++;
            }
        }

        int[] arr2 = new int[N];
        for (int i = 0; i < N; i++)
            arr2[i] = start[i];
        arr2[0] = (arr2[0] + 1) % 2;
        arr2[1] = (arr2[1] + 1) % 2;
        int answer2 = 1;
        for (int i = 1; i < N; i++) {
            if (arr2[i-1] != goal[i-1]) {
                arr2[i-1] = (arr2[i-1] + 1) % 2;
                arr2[i] = (arr2[i] + 1) % 2;
                if (i != N-1)
                    arr2[i+1] = (arr2[i+1] + 1) % 2;
                answer2++;
            }
        }

        int result = 999999999;
        if (arr[N-1] == goal[N-1])
            result = Math.min(answer, result);
        if (arr2[N-1] == goal[N-1])
            result = Math.min(answer2, result);

        if (result != 999999999)
            System.out.println(result);
        else
            System.out.println(-1);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());

        start = new int[N];
        goal = new int[N];

        String st = bf.readLine();
        String go = bf.readLine();
        for (int i = 0; i < N; i++){
            start[i] = st.charAt(i) - '0';
            goal[i] = go.charAt(i) - '0';
        }

        check();
    }
}