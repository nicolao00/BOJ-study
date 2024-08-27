import java.util.*;
import java.io.*;

//1118
class Main {
    static int N;
    static int M;
    static StringBuilder staticSb = new StringBuilder();

    static void makePermut(StringBuilder sb) {
        if (sb.length() / 2 == M) {
            if (sb.length() != 1)
                sb.deleteCharAt(sb.length() - 1);
            staticSb.append(sb).append('\n');
            return;
        }

        for (int i = 1; i <= N; i++) {
            StringBuilder newSb = new StringBuilder(sb.toString());
            newSb.append(i);
            newSb.append(' ');
            makePermut(newSb);
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        makePermut(new StringBuilder());
        staticSb.deleteCharAt(staticSb.length() - 1);
        bw.write(staticSb.toString());
        bw.newLine(); // 줄바꿈
        bw.flush(); // 남아있는 데이터 모두 출력
        bw.close();
    }
}