import java.util.*;
import java.io.*;

// 600
class Main {
    static int N;

    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        HashMap<String, int[]> commands = new HashMap<>();
        commands.put("R", new int[]{0, 1}); commands.put("L", new int[]{0, -1});
        commands.put("T", new int[]{1, 0}); commands.put("B", new int[]{-1, 0});
        commands.put("RB", new int[]{-1, 1}); commands.put("LB", new int[]{-1, -1});
        commands.put("RT", new int[]{1, 1}); commands.put("LT", new int[]{1, -1});

        StringTokenizer st = new StringTokenizer(bf.readLine());
        String king = st.nextToken();
        String rock = st.nextToken();
        N = Integer.parseInt(st.nextToken());

        int kC = king.charAt(0) - 'A';
        int kR = king.charAt(1) - '1';
        int rC = rock.charAt(0) - 'A';
        int rR = rock.charAt(1) - '1';
        for (int i = 0; i < N; i++) {
            int[] drdc = commands.get(bf.readLine());
            kR += drdc[0];
            kC += drdc[1];

            if (0 > kR || kR >= 8 || 0 > kC || kC >= 8) {
                kR -= drdc[0];
                kC -= drdc[1];
                continue;
            }

            if (kR == rR && kC == rC) {
                rR += drdc[0];
                rC += drdc[1];
                if (0 > rR || rR >= 8 || 0 > rC || rC >= 8) {
                    kR -= drdc[0];
                    kC -= drdc[1];
                    rR -= drdc[0];
                    rC -= drdc[1];
                }
            }
        }

        String[] str = new String[]{"A", "B", "C", "D", "E", "F", "G", "H"};
        StringBuilder sb = new StringBuilder();
        sb.append(str[kC]); sb.append(kR+1); sb.append('\n');
        sb.append(str[rC]); sb.append(rR + 1);
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
