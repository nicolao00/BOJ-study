import java.util.*;
import java.io.*;


// 832
class Main {
    static int N;
    static int[] board;
    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        board = new int[N];

        StringTokenizer st = new StringTokenizer(bf.readLine());
        for (int i = 0; i < N; i++) {
            board[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(board);

        int left = 0;
        int right = N-1;
        int min = 0;
        int max = 0;
        int result = 0;
        int answer = 2000000000;
        while (left < right) {
            result = board[left] + board[right];
            if (answer > Math.abs(result)) {
                min = left;
                max = right;
                answer = Math.abs(result);
            }

            if (result > 0) {
                right--;
            } else if (result < 0) {
                left++;
            } else {
                StringBuilder sb = new StringBuilder();
                sb.append(board[left]).append(' ').append(board[right]);
                System.out.println(sb.toString());
                break;
            }
        }
        StringBuilder sb = new StringBuilder();
        sb.append(board[min]).append(' ').append(board[max]);
        System.out.println(sb.toString());
    }
}