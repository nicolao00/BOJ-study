import java.io.*;
import java.util.*;

// 900
public class Main {
    static int R, C, N;
    static char[][] board;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};
    static int[][] timerBoard;
    static int[][] tmpBoard;

    static void timerCount() {
        int[][] tmp = new int[R][C];
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (timerBoard[r][c] == 1) {
                    tmp[r][c] = 0;
                    for (int i = 0; i < 4; i++) {
                        int nr = r + dr[i];
                        int nc = c + dc[i];
                        if (0 <= nr && nr < R && 0 <= nc && nc < C) {
                            if (timerBoard[nr][nc] > 1)
                                timerBoard[nr][nc] = -1;
                            tmp[nr][nc] = 0;
                        }
                    }
                }
                else if (timerBoard[r][c] > 1)
                    tmp[r][c] = timerBoard[r][c] - 1;
                    // 폭탄 터졌던 자리
                else
                    tmp[r][c] = 0;
            }
        }
        timerBoard = tmp;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        board = new char[R][C];
        timerBoard = new int[R][C];

        for (int i = 0; i < R; i++)
            board[i] = bf.readLine().toCharArray();

        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (board[r][c] == 'O') {
                    timerBoard[r][c] = 2;
                }
            }
        }

        int t = 1;
        while (t < N) {
            // 다음 1초 동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다. + 3초 됐으면 폭파
            tmpBoard = new int[R][C];
            for (int r = 0; r < R; r++) {
                for (int c = 0; c < C; c++) {
                    // 폭탄 설치
                    if (timerBoard[r][c] == 0)
                        tmpBoard[r][c] = 3;
                    // 3초가 된 폭탄
                    else if (timerBoard[r][c] == 1) {
                        tmpBoard[r][c] = 0;
                        for (int i = 0; i < 4; i++) {
                            int nr = r + dr[i];
                            int nc = c + dc[i];
                            if (0 <= nr && nr < R && 0 <= nc && nc < C) {
                                // 폭탄 연쇄작용 없애기
                                if (timerBoard[nr][nc] > 1)
                                    timerBoard[nr][nc] = -1;
                                tmpBoard[nr][nc] = 0;
                            }
                        }
                    }
                    // 폭탄 연쇄작용 제외하기위해 else가 아닌 else if로
                    else if (timerBoard[r][c] > 1)
                        tmpBoard[r][c] = timerBoard[r][c] - 1;
                    else
                        tmpBoard[r][c] = 0;
                }
            }
            timerBoard = tmpBoard;
            t++;

            if (t >= N)
                break;
            // 1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발한다.
            timerCount();
            t++;
        }

        StringBuilder sb = new StringBuilder();
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (timerBoard[r][c] > 0)
                    sb.append('O');
                else
                    sb.append('.');
            }
            sb.append('\n');
        }
        sb.deleteCharAt(sb.length() - 1);
        System.out.println(sb.toString());
    }
}