import java.util.*;
class Solution {//TODO: improve pls
    public static void shortestToChar(String S, char C) {
        ArrayList<Integer> myList = new ArrayList<>();
        for(int i =0 ;i<S.length();i++)
        {
            if (S.charAt(i) == C)
                myList.add(i);
        }
        System.out.println(Arrays.toString(myList.toArray()));
        // int j =0 ;
        // int arr[]=new int[S.length()];
        // for (int i = 0;i<S.length();i++)
        // {
        //     arr[i] = Math.abs(myList.get(j) - i);
        //     if(i==myList.get(j)) {
        //         j++;
        //     }
        // }
        // return arr;
    }
    public static void main(String[] args) {
        // System.out.println(Arrays.toString(shortestToChar("loveleetcode", 'e')));
        shortestToChar("loveleetcode", 'e');
    }
}