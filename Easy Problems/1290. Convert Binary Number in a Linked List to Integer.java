/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int getDecimalValue(ListNode head) {
        ListNode c = new ListNode(0);
        c = head;
        String val = "";
        double sum = 0;
        while(c != null)
        {
            val = val + String.valueOf(c.val);
            c = c.next;
        }
        for (int i = 0,j = val.length() - 1; i < val.length() && j >= 0;i++, j--)
        {
            sum = sum + (Character.getNumericValue(val.charAt(i)))*Math.pow(2,j);
        }
        return (int)sum;
    }
}