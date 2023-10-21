/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode lhs, ListNode rhs) {
        var dummy = new ListNode();
        var tail = dummy;
        
        while (lhs != null && rhs != null) {
            if(lhs.val < rhs.val) {
                tail.next = lhs;
                lhs = lhs.next;
            } else {
                tail.next = rhs;
                rhs = rhs.next;
            }
            tail = tail.next;
        }
        if (lhs != null) {
            tail.next = lhs;
        } else {
            tail.next = rhs;
        }

        return dummy.next;
    }
}