import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        StringBuilder answer = new StringBuilder();
        
        String[] nums = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++){
            nums[i] = String.valueOf(numbers[i]);
        }
        
        Arrays.sort(nums, (o1, o2) -> ((o2+o1).compareTo(o1+o2)));
        
        for (int i = 0; i < numbers.length; i++){
            answer.append(nums[i]);
        }
        String ans = answer.toString();
        if (ans.charAt(0) == '0') return "0";
        return ans;
    }
}

/*
//1030 - 1110   1120/
import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        StringBuilder answer = new StringBuilder();
        String[] nums = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++){
            nums[i] = String.valueOf(numbers[i]);
        }
        
        Arrays.sort(nums, (o1, o2) -> (o2.compareTo(o1)));
        
        for (int i = 0; i < numbers.length; i++){
            answer.append(nums[i]);
        }
        
        return answer.toString();
    }
}


/*

31 9 3 2 2
9 3 2 

52 9 5 3

524 5 1 3

351 2 32 
 
 */