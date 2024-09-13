import java.io.*;
import java.util.*;

// 1123
public class Main {
    static ArrayList<Node>[] childs;
    static int nodeCnt;
    static int max;
    static int maxIdx;
    static boolean[] visit;




    static void dfs(int start, int dist) {
        if (max < dist){
            max = dist;
            maxIdx = start;
        }

        for (Node child : childs[start]) {
            if (!visit[child.child]) {
                visit[child.child] = true;
                dfs(child.child, dist + child.weight);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        nodeCnt = Integer.parseInt(bf.readLine());
        childs = new ArrayList[nodeCnt+1];
        for (int i = 0; i < nodeCnt + 1; i++) {
            childs[i] = new ArrayList<>();
        }

        for (int i = 1; i < nodeCnt; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int parent = Integer.parseInt(st.nextToken());
            int child = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());
            childs[parent].add(new Node(child, dist));
            childs[child].add(new Node(parent, dist));
        }

        max = 0;
        visit = new boolean[nodeCnt + 1];
        visit[1] = true;
        dfs(1, 0);

        visit = new boolean[nodeCnt + 1];
        visit[maxIdx] = true;
        dfs(maxIdx, 0);

        System.out.println(max);
    }
}
class Node {
    public int child;
    public int weight;

    Node(int child, int weight) {
        this.child = child;
        this.weight = weight;
    }
}