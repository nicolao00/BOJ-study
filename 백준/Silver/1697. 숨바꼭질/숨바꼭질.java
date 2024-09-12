import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());
        int k=Integer.parseInt(st.nextToken());
        System.out.println(dfs(n,k));
    }

    static int dfs(int n,int k) {

        if(n>=k) return n-k;
        if(k==1) return 1;
        if(k%2==1) return Math.min(dfs(n,k+1),dfs(n,k-1))+1;     
        return Math.min(k-n,dfs(n,k/2)+1);
    }
}