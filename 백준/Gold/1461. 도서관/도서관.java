import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;


public class Main {
    static int N,M;
    static int[] books;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        books = new int[N];

        ArrayList<Integer> positiveBooks = new ArrayList<>();
        ArrayList<Integer> negativeBooks = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            int value = Integer.parseInt(st.nextToken());
            books[i] = value;
            if (value > 0)
                positiveBooks.add(value);
            else
                negativeBooks.add(value);
        }

        Collections.sort(positiveBooks, Collections.reverseOrder());
        Collections.sort(negativeBooks);

        int positiveSum = 0;
        int i = 0;
        while (i < positiveBooks.size()) {
            positiveSum += positiveBooks.get(i) * 2;
            i += M;
        }

        int negativeSum = 0;
        i = 0;
        while (i < negativeBooks.size()) {
            negativeSum += negativeBooks.get(i) * 2;
            i += M;
        }

        System.out.println(Math.min(positiveSum + Math.abs(negativeSum) - ((positiveBooks.size() > 0) ? positiveBooks.get(0) : 0), positiveSum + Math.abs(negativeSum) + ((negativeBooks.size() > 0) ? negativeBooks.get(0) : 0)));
    }
}