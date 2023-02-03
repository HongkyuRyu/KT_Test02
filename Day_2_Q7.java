import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        
        int a  = -1;
        ArrayList<Integer> arr1 = new ArrayList<Integer>();
        
        for(int idx: arr){
            if (a != idx) {
                arr1.add(idx);
            }
            a= idx;
        }
        answer = new int[arr1.size()];
        for(int i=0; i<answer.length; i++){
            answer[i] = arr1.get(i);
            //System.out.println(answer[i]);
        }
        
        return answer;
        
        
    }