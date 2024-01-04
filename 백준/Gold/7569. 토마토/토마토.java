import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static int[][][] box;
    public static boolean[][][] visit;
    public static int M, N, H;
    public static Queue<Node> queue = new LinkedList<>();
    public static Change[] changes = {
            new Change(0, 0, 1),
            new Change(0, 0, -1),
            new Change(1, 0, 0),
            new Change(-1, 0, 0),
            new Change(0, 1, 0),
            new Change(0, -1, 0)
    };
    static class Change {
        int x, y, z;
        Change(int x, int y, int z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }
    }
    static class Node {
        int x, y, z, d;
        Node(int x, int y, int z, int d) {
            this.x = x;
            this.y = y;
            this.z = z;
            this.d = d;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        StringBuilder sb = new StringBuilder();

        M = Integer.parseInt(st.nextToken()); 
        N = Integer.parseInt(st.nextToken()); 
        H = Integer.parseInt(st.nextToken()); 

        box = new int[H][N][M];
        visit = new boolean[H][N][M];

        boolean flag = true;
        for (int h = 0; h < H; h++) {
            for (int n = 0; n < N; n++) {
                st = new StringTokenizer(br.readLine(), " ");
                for (int m = 0; m < M; m++) {
                    int value = Integer.parseInt(st.nextToken());
                    if (value == 1)
                        queue.add(new Node(m, n, h, 0));
                    else if (value == 0)
                        flag = false;
                    box[h][n][m] = value;
                }
            }
        }
        if (flag){
            System.out.println(0);
            return;
        }

        int answer = 0;
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            int x = node.x, y = node.y, z = node.z, d = node.d;
            answer = d;
            visit[z][y][x] = true;

            for (Change change : changes) {
                int nx = x + change.x, ny = y + change.y, nz = z + change.z;
                if (0 <= nx && nx < M && 0 <= ny && ny < N && 0 <= nz && nz < H) {
                    if (box[nz][ny][nx] == 0) {
                        if (!visit[nz][ny][nx]) {
                            box[nz][ny][nx] = 1;
                            queue.add(new Node(nx, ny, nz, d + 1));
                            visit[nz][ny][nx] = true;
                        }
                    }
                }
            }
        }

        for (int h = 0; h < H; h++) {
            for (int n = 0; n < N; n++) {
                for (int m = 0; m < M; m++){
                        if (box[h][n][m] == 0) {
                            System.out.println(-1);
                            return;
                        }
                }
            }
        }
        System.out.println(answer);
    }
}