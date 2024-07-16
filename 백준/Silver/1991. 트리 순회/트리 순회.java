import java.util.*;
import java.io.*;

class Main {
    static int N;
    static Map<Character, Character[]> tree;
    static StringBuilder sb;

    public static void preOrder(char start) {
        sb.append(start);
        if (tree.get(start)[0] != '.')
            preOrder(tree.get(start)[0]);
        if (tree.get(start)[1] != '.')
            preOrder(tree.get(start)[1]);
    }

    public static void inOrder(char start) {
        if (tree.get(start)[0] != '.') {
            inOrder(tree.get(start)[0]);
        }
        sb.append(start);
        if (tree.get(start)[1] != '.')
            inOrder(tree.get(start)[1]);
    }

    public static void postOrder(char start) {
        if (tree.get(start)[0] != '.') {
            postOrder(tree.get(start)[0]);
        }
        if (tree.get(start)[1] != '.') {
            postOrder(tree.get(start)[1]);
        }
        sb.append(start);
    }

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        tree = new HashMap<>();

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            char node = st.nextToken().charAt(0);
            tree.put(node, new Character[]{
                    st.nextToken().charAt(0), st.nextToken().charAt(0)
            });
        }
        sb = new StringBuilder();
        preOrder('A');
        System.out.println(sb.toString());

        sb = new StringBuilder();
        inOrder('A');
        System.out.println(sb.toString());

        sb = new StringBuilder();
        postOrder('A');
        System.out.println(sb.toString());
    }
}