// 1026
import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main{
    // 소유한 랜선의 개수, 필요한 랜선의 개수
    static int K, N;
    static long[] lens;

    static long slides(long mid) {
        long result = 0;

        for (int i = 0; i < K; i++){
            result += lens[i] / mid;
        }
        return result;
    }

    public static void main(String args[]) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        // N: 세로
        K = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        lens = new long[K];

        for (int i = 0; i < K; i++)
            lens[i] = Integer.parseInt(bf.readLine());
        Arrays.sort(lens);

        long left = 1;
        long right = lens[K-1];
        long mid = (left + right)/2;
        while (left <= right) {
            mid = (left + right)/2;
            long result = slides(mid);

            if (result >= N){
                left = mid + 1;
            } else if (result < N) {
                right = mid - 1;
            }
        }
        System.out.println(Long.toString(right));
    }
}
//1 1
//2147483647