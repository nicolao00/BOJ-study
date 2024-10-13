import java.io.*;
import java.net.Inet4Address;
import java.util.*;

// 328
public class Main {
    static int K;

    public static void main(String[] args) throws Exception {
        K = read();
        int[] lengths = new int[5];
        int[][] inputs = new int[6][2];

        for (int i = 0; i < 6; i++) {
            inputs[i][0] = read();
            inputs[i][1] = read();
            lengths[inputs[i][0]] += inputs[i][1];
        }

        int[] endNodes = new int[2];
        int t = 0;
        for (int i = 0; i < 6; i++) {
            if (lengths[1] == inputs[i][1] || lengths[3] == inputs[i][1]) {
                endNodes[t++] = i;
            }
        }

        if (endNodes[0] == 0 && endNodes[1] == 5) {
            endNodes[0] = 2;
            endNodes[1] = 3;
        }
        else {
            endNodes[0] = (endNodes[0] - 2) < 0 ? 6 + (endNodes[0] - 2) : endNodes[0] - 2;
            endNodes[1] = (endNodes[1] + 2) % 6;
        }

        int fieldSize = lengths[1] * lengths[3] - inputs[endNodes[0]][1] * inputs[endNodes[1]][1];
        System.out.println(fieldSize * K);
    }

    private static int read() throws Exception {
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32) {
            n = (n << 3) + (n << 1) + (c & 15);
        }
        return n;
    }
}