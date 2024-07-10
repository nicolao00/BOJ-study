// 119
import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String str = bf.readLine();

        Stack<StringBuilder> nums = new Stack<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (c == '(') {
                nums.add(sb);
                sb = new StringBuilder();
            }
            else if (c == ')'){
                nums.add(sb);
                break;
            }
            else
                sb.append(c);
        }

        int answer = nums.pop().length();
        while (!nums.isEmpty()) {
            StringBuilder num = nums.pop();
            answer *= num.charAt(num.length() - 1) - '0';
            if (num.length() > 1)
                answer += num.length() - 1;
        }
        System.out.println(answer);
    }
}