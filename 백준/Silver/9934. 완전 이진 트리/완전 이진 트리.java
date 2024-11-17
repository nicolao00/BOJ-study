// 043
import java.util.*;
import java.io.*;

class Main {
    static int K;
    static ArrayList<Integer>[] depthNodes;
    static int[] visitSeq;

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        K = Integer.parseInt(bf.readLine());

        int nodeCnt = (int)Math.pow(2, K) - 1;
        visitSeq = new int[nodeCnt];
        depthNodes = new ArrayList[K];
        for (int i = 0; i < K; i++)
            depthNodes[i] = new ArrayList<>();

        StringTokenizer st = new StringTokenizer(bf.readLine());
        for (int i = 0; i < nodeCnt; i++){
            visitSeq[i] = Integer.parseInt(st.nextToken());
        }

        search(0, nodeCnt, 0);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < K; i++) {
            for (int a : depthNodes[i]) {
                sb.append(a).append(' ');
            }
            sb.append('\n');
        }
        System.out.println(sb.toString());
    }

    static void search(int start, int end, int depth){
        if (depth == K)
            return;

        int mid = (start + end)/2;
        depthNodes[depth].add(visitSeq[mid]);

        search(start, mid, depth+1);
        search(mid, end, depth+1);
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