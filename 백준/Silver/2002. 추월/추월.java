import java.util.*;
import java.io.*;

class Main {
    static int N;
    static String[] cars;
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        cars = new String[N];

        for (int i = 0; i < N; i++) {
            cars[i] = bf.readLine();
        }

        int answer = 0;
        int result = 0;
        Set<String> set = new HashSet<>();
        for (int i = 0; i < N; i++) {
            String str = bf.readLine();
            set.add(str);
            if (str.equals(cars[answer]))
                answer++;
            while (answer < N && set.contains(cars[answer])) {
                answer++;
                result++;
            }
        }
        System.out.println(result);
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