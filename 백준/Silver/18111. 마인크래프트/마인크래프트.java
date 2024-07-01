import java.io.*;
import java.util.*;

public class Main {
    // 1151

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        // 세로, 가로, 높이
        int N, M, B;
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        int answer = 99999999;
        int height = -1;

        int[][] board = new int[N][M];

        int total = B;
        int maxV = -1;
        int minV = 257;
        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(bf.readLine());
            for (int c = 0; c < M; c++) {
                int tmp = Integer.parseInt(st.nextToken());
                maxV = Math.max(maxV, tmp);
                minV = Math.min(minV, tmp);
                total += tmp;
                board[r][c] = tmp;
            }
        }
        maxV = total / (M*N);

        for (int v = minV; v <= maxV; v++){
            int result = 0;
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < M; c++) {
                    int diff = board[r][c] - v;
                    // 추가
                    if (diff < 0)
                        result += Math.abs(diff);
                        // 제거
                    else
                        result += diff*2;

                }
            }
            if (answer > result || (answer == result && height < v)){
                answer = result;
                height = v;
            }
        }
        System.out.println(String.valueOf(answer) + ' ' + String.valueOf(height));
    }
}