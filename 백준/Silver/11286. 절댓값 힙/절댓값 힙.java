import java.io.*;
import java.util.*;

// 224
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int operateCnt = Integer.parseInt(bf.readLine());


        PriorityQueue<Integer> pq = new PriorityQueue<>((o1, o2) -> {
            int firstCondition = Integer.compare(Math.abs(o1), Math.abs(o2));
            if (firstCondition != 0) {
                return firstCondition;
            } else {
                return Integer.compare(o1, o2);
            }
        });
        for (int i = 0; i < operateCnt; i++) {
            int value = Integer.parseInt(bf.readLine());
            if (value != 0)
                pq.offer(value);
            else {
                if (pq.size() != 0)
                    bw.write(String.valueOf(pq.poll()));
                else
                    bw.write(String.valueOf(0));
                if (i < operateCnt - 1) {
                    bw.write('\n');
                }
            }
        }

        bw.flush();
        bw.close();
    }
}