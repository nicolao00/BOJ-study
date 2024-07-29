import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String str = bf.readLine();
        Stack<Object> stack = new Stack<>();

        for (int i = 0; i < str.length(); i++) {
            char word = str.charAt(i);
            boolean flag = false;

            if (word == '(' || word == '[')
                stack.add(word);
            else {
                int value = 0;
                while (!stack.isEmpty()) {
                    Object tmp = stack.pop();

                    // 그 전 값에 숫자가 있다 (더함)
                    if (tmp instanceof Integer)
                        value += (Integer) tmp;
                     // 그 전 값이 괄호이다.
                    else if (tmp instanceof Character){
                        char exWord = (Character) tmp;
                        // 그  전 값이 같은 괄호가 아니다
                        if ((exWord == '(' && word != ')') || (exWord == '[' && word != ']')){
                            System.out.println(0);
                            return;
                        }
                        else {
                            if (value == 0)
                                value = 1;

                            flag = true;
                            stack.add(word == ')' ? value * 2 : value * 3);
                            break;
                        }
                    }
                }
                if (!flag) {
                    System.out.println(0);
                    return;
                }
            }
        }

        int answer = 0;
        while (!stack.isEmpty()) {
            Object exWord = stack.pop();
            if (exWord instanceof Integer)
                answer += (Integer) exWord;
            else {
                System.out.println(0);
                return;
            }
        }
        System.out.println(answer);
    }
}