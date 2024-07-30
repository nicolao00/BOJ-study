import java.util.*;
import java.io.*;

class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String str = bf.readLine();

        LinkedList<Character> linkedList = new LinkedList<>();
        ListIterator<Character> iterator = linkedList.listIterator();
        for (int i = 0; i < str.length(); i++)
            iterator.add(str.charAt(i));

        int testCase = Integer.parseInt(bf.readLine());
        for (int t = 0; t < testCase; t++) {
            String[] commend = bf.readLine().split(" ");

            if (commend.length == 1){
                switch (commend[0]) {
                    case "L":
                        if (iterator.hasPrevious())
                            iterator.previous();
                        break;
                    case "D":
                        if (iterator.hasNext())
                            iterator.next();
                        break;
                    case "B":
                        if (iterator.hasPrevious()) {
                            iterator.previous();
                            iterator.remove();
                        }
                        break;
                }
            }
            else {
                iterator.add(commend[1].charAt(0));
            }
        }

        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
        for (char a : linkedList) {
            bufferedWriter.write(a);
        }
        bufferedWriter.flush();
    }
}