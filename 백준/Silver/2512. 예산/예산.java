import java.util.*;
import java.io.*;
 
class Main {
    static int N;
    static int[] cost;
    static int M;
    static int totalCost;

    public static void binarySearch(int maxValue) {
        if (totalCost > M) {
            int l = 1;
            int r = maxValue;
            while (l <= r) {
                int mid = (l + r) / 2;
                int result = 0;
                for (int i = 0; i < N; i++)
                    result += cost[i] > mid ? mid : cost[i];
                if (result > M)
                    r = mid - 1;
                else
                    l = mid + 1;
            }
            System.out.println(r);
        }
        else
            System.out.println(maxValue);

    }

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        cost = new int[N];

        int maxValue = 0;
        StringTokenizer st = new StringTokenizer(bf.readLine());
        for (int i = 0; i < N; i++) {
            cost[i] = Integer.parseInt(st.nextToken());
            totalCost += cost[i];
            maxValue = Math.max(maxValue, cost[i]);
        }
        M = Integer.parseInt(bf.readLine());
        binarySearch(maxValue);
    }
}