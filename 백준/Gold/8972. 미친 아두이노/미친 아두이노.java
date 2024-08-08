import java.util.*;
import java.io.*;

//453 - 559
class Main {
    static int R;
    static int C;
    static char[][] board;
    static int[] jongsu;
    static Set<String> crazy = new HashSet<>();
    static int[] dr = {0, 1, 1, 1, 0, 0, 0, -1, -1, -1};
    static int[] dc = {0, -1, 0, 1, -1, 0, 1, -1, 0, 1};

    public static boolean bfs(int idx) {
        jongsu[0] += dr[idx];
        jongsu[1] += dc[idx];
        if (crazy.contains(jongsu[0] + "," + jongsu[1]))
            return false;

        Set<String> newCrazy = new HashSet<>();
        ArrayList<String> removeRC = new ArrayList<>();
        for (String rc : crazy) {
            String[] parts = rc.split(",");

            int min = 9999999;
            int[] newRC = new int[]{-1, -1};
            for (int i = 1; i <= 9; i++) {
                int nr = Integer.parseInt(parts[0]) + dr[i];
                int nc = Integer.parseInt(parts[1]) + dc[i];
                if (nr < 0 || nr >= R || nc < 0 || nc >= C)
                    continue;
                int result = Math.abs(jongsu[0] - nr) + Math.abs(jongsu[1] - nc);
                if (result < min){
                    min = result;
                    newRC[0] = nr;
                    newRC[1] = nc;
                }
            }

            if (jongsu[0] == newRC[0] && jongsu[1] == newRC[1])
                return false;
            String tmp = newRC[0] + "," + newRC[1];

            if (!newCrazy.contains(tmp))
                newCrazy.add(tmp);
            else
                removeRC.add(tmp);
        }
        for (String str : removeRC)
            newCrazy.remove(str);
        crazy = newCrazy;
        return true;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        board = new char[R][C];
        jongsu = new int[2];

        for (int i = 0 ; i < R; i++) {
            char[] tmp = bf.readLine().toCharArray();
            for (int j = 0; j < C; j++) {
                if (tmp[j] == 'R')
                    crazy.add(i + "," + j);
                else if (tmp[j] == 'I') {
                    jongsu[0] = i;
                    jongsu[1] = j;
                }
            }
            board[i] = tmp;
        }

        String dir = bf.readLine();
        int idx = 0;
        while (idx < dir.length() && bfs(dir.charAt(idx) - '0'))
            idx++;

        if (idx != dir.length())
            System.out.println("kraj " + (idx+1));
        else {
            for (int i = 0; i < R; i++)
                Arrays.fill(board[i], '.');
            board[jongsu[0]][jongsu[1]] = 'I';
            for (String rc : crazy) {
                String[] parts = rc.split(",");
                int r = Integer.parseInt(parts[0]);
                int c = Integer.parseInt(parts[1]);
                board[r][c] = 'R';
            }

            for (int r = 0; r < R; r++) {
                StringBuilder sb = new StringBuilder();
                for (int c = 0; c < C; c++)
                    sb.append(board[r][c]);
                System.out.println(sb.toString());
            }
        }
    }
}