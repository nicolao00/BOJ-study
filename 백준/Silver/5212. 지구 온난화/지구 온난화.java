import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(bf.readLine());
        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        char[][] board = new char[R][];
        char[][] newBoard = new char[R][];
        int minR = 10;
        int minC = 10;
        int maxR = -1;
        int maxC = -1;

        for (int r = 0; r < R; r++) {
            String tmp = bf.readLine();
            board[r] = tmp.toCharArray();
            newBoard[r] = tmp.toCharArray();
        }

        int[] dr = new int[]{-1, 0, 1, 0};
        int[] dc = new int[]{0, 1, 0, -1};
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                int islandCnt = 0;
                for (int i = 0; i < 4; i++) {
                    int nr = r + dr[i];
                    int nc = c + dc[i];
                    if (0 <= nr && nr < R && 0 <= nc && nc < C && board[nr][nc] == 'X'){
                        islandCnt++;
                    }
                }
                if (islandCnt < 2) {
                    newBoard[r][c] = '.';
                }
                if (newBoard[r][c] == 'X') {
                    minR = Math.min(minR, r);
                    minC = Math.min(minC, c);
                    maxR = Math.max(maxR, r);
                    maxC = Math.max(maxC, c);
                }
            }
        }

        for (int r = minR; r <= maxR; r++) {
            StringBuilder sb = new StringBuilder();
            for (int c = minC; c <= maxC; c++){
                sb.append(newBoard[r][c]);
            }
            System.out.println(sb.toString());
        }
    }
}