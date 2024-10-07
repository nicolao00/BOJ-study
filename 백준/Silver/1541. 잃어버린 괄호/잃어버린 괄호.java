import java.io.*;
import java.util.*;
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String str = bf.readLine();

        Queue<Integer> q = new ArrayDeque<>();
        for (String st : str.split("\\+|-")) {
            q.offer(Integer.valueOf(st));
        }

        int answer = q.poll();
        int minusValue = 0;
        boolean flag = false;
        for (int i = 0; i < str.length(); i++) {
            // -가 이미 나왔을 때
            if (flag) {
                char character = str.charAt(i);
                if (character == '+' || character == '-')
                    minusValue += q.poll();
            }
            else {
                if (str.charAt(i) == '+')
                    answer += q.poll();
                else if (str.charAt(i) == '-') {
                    flag = true;
                    minusValue += q.poll();
                }
            }
        }
        System.out.println(answer - minusValue);
    }
}