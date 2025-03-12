// 1128

import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        String startTime = st.nextToken();
        String endTime = st.nextToken();
        String quitTime = st.nextToken();

        Set<String> IN = new HashSet<>();
        Set<String> OUT = new HashSet<>();

        String line;
        while ((line = bf.readLine()) != null && !line.isEmpty()) {
            st = new StringTokenizer(line);
            String time = st.nextToken();
            String name = st.nextToken();
            if (time.compareTo(startTime) <= 0) {
                IN.add(name);
            } else if (time.compareTo(endTime) >= 0 && time.compareTo(quitTime) <= 0) {
                OUT.add(name);
            }
        }

        int answer = 0;
        for (String name : IN) {
            if (OUT.contains(name)) {
                answer += 1;
            }
        }
        System.out.println(answer);
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