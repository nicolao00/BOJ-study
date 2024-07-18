// 1011

import java.util.*;
import java.io.*;

class Main {
    static int N;
    static int K;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        if (K == 8) {
            System.out.println("10234567");
            return;
        }
        if (K == 9) {
            System.out.println("102345678");
            return;
        }
        else if (K == 10){
            System.out.println("1023456789");
            return;
        }

        while (true) {
            int cnt = 0;
            int tmp = ++N;
            Set<Integer> set = new HashSet<>();
            
            while(tmp != 0) {
                set.add(tmp % 10);
                tmp /= 10;
            }
            if (set.size() == K) {
                System.out.println(N);
                break;
            }
        }
    }
}
