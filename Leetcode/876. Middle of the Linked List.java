/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode x = head;
        int c = 0;
        while(x != null)
        {
            x = x.next;
            c ++;
        }
        ListNode k = head;
        if (c%2 == 1)
        {
            for(int i =1 ;i<=c/2;i++)
                k = k.next;
            return k;
        }
        else
        {
            for(int i =1;i<=c/2;i++)
                k = k.next;
            return (k);
        }
    }
}