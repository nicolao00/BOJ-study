// 1106

import java.io.*; 
import java.util.*;

class Main {
    static int N;
    static int[][] board;
    static int[][] distBoard;
    static int[][] wordLoc;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public static void bfs() {

        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[2] - o2[2]);
        pq.offer(new int[]{0, 0, 0});

        int wordIdx = 0;
        if (wordLoc[wordIdx][0] == 0 && wordLoc[wordIdx][1] == 0) {
            wordIdx++;
            pq.clear();
        }
        int goalValue = 0;
        while (wordIdx < 5) {
            if (wordIdx > 0) {
                pq.offer(new int[]{wordLoc[wordIdx - 1][0], wordLoc[wordIdx - 1][1], goalValue});
                for (int i = 0; i < N; i++) 
                    Arrays.fill(distBoard[i], 1000001);
                distBoard[wordLoc[wordIdx - 1][0]][wordLoc[wordIdx - 1][1]] = goalValue;
            }
            goalValue = 1000001;
                
            
            while (!pq.isEmpty()) {
                int[] rcd = pq.poll();
                int r = rcd[0];
                int c = rcd[1];
                int d = rcd[2];

                for (int i = 0; i < 4; i++) {
                    int nr = r + dr[i];
                    int nc = c + dc[i];
                    if (0 <= nr && nr < N && 0 <= nc && nc < N && d + board[r][c] + board[nr][nc] < distBoard[nr][nc]) {
                        distBoard[nr][nc] = d + board[r][c] + board[nr][nc];
                        if (nr == wordLoc[wordIdx][0] && nc == wordLoc[wordIdx][1])
                            goalValue = Math.min(goalValue, distBoard[nr][nc]);
                        else
                            pq.offer(new int[]{nr, nc, distBoard[nr][nc]});
                    }
                }
            }
            wordIdx++;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        board = new int[N][N];
        distBoard = new int[N][N];
        for (int i = 0; i < N; i++) 
            Arrays.fill(distBoard[i], 1000001);
        wordLoc = new int[5][2];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            for (int j = 0; j < N; j++){
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < 5; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            wordLoc[i][0] = Integer.parseInt(st.nextToken()) - 1;
            wordLoc[i][1] = Integer.parseInt(st.nextToken()) - 1;
        }
         
        bfs();
        int answer = distBoard[wordLoc[4][0]][wordLoc[4][1]];
        int[] tmp = new int[] {wordLoc[4][0], wordLoc[4][1]};
        wordLoc[4][0] = wordLoc[0][0];
        wordLoc[4][1] = wordLoc[0][1];
        wordLoc[0][0] = tmp[0];
        wordLoc[0][1] = tmp[1];
        bfs();
        System.out.println(Math.min(answer, distBoard[wordLoc[4][0]][wordLoc[4][1]]));
    }
}