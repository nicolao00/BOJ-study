import java.util.*;
import java.io.*;


// 1007
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        String input = bf.readLine();
        StringBuilder sb = new StringBuilder();
        StringBuilder tmp = new StringBuilder();
        int openCnt = 0;
        boolean flag = false;
        // 일단 기록
        // 1. < 나오면 플래그 1++
        //   1-1 flag == 0이면 지금까지한거 기록
        // 2. 공백 나오면
        //   2-1 플래그없는 경우: 기록한거 반영
        //   2-2 플래그있는 경우: 이어서 기
        // 3. > 나오면 플래그 1--
        //   3-1 플래그 0되면 기록
        // 남은거 다 기록
        for (int i = 0; i < input.length(); i++) {
            char ch = input.charAt(i);
            if (ch == '<') {
                if (!flag) {
                    sb.append(tmp.reverse());
                    tmp = new StringBuilder();
                }
                tmp.append(ch);
                flag = true;
                openCnt++;
            } else if (ch == '>') {
                openCnt--;
                tmp.append(ch);
                if (openCnt == 0) {
                    sb.append(tmp);
                    tmp = new StringBuilder();
                    flag = false;
                }
            } else if (ch == ' ') {
                if (!flag) {
                    sb.append(tmp.reverse()).append(ch);
                    tmp = new StringBuilder();
                    continue;
                } else {
                    tmp.append(ch);
                }
            } else
                tmp.append(ch);
        }
        sb.append(tmp.reverse());
        System.out.println(sb.toString());
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
