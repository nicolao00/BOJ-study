import java.util.*;
import java.io.*;


// 1007
class Main {
    static int N;
    static int count;
    static boolean flag;
    static char[] chars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};

    public static void main(String[] args) throws IOException{
        count = 0;
        N = read();
        flag = true;
        if (N == 1) {
            System.out.println("0");
            return;
        } else
            N -= 1;

        for (int len = 1; len <= 10; len++) {
            for (int start = 1; start <= 9; start++) {
                if (count < N)
                    back_tracking(new StringBuilder(String.valueOf(start)), start, len);
            }
        }
        if (flag)
            System.out.println("-1");
    }

    static void back_tracking(StringBuilder sb, int idx, int len) {
        if (len == sb.length()) {
            count++;
            if (count == N) {
                flag = false;
                System.out.println(sb.toString());
            }
            return;
        }

        for (int i = 0; i < idx; i++) {
            sb.append(chars[i]);
            back_tracking(sb, i, len);
            sb.deleteCharAt(sb.length() - 1);
        }
    }

    // 걍 띄워쓰기 기준으로 다 하나씩 숫자 입력받는 듯?
    private static int read() throws IOException {
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32) {
            n = (n << 3) + (n << 1) + (c & 15);
        }
        return n;
    }
}
