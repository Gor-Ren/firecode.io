import java.util.Optional;

/**
 * Given a singly-linked list, implement a method to delete the node at a given position (starting
 * from 1 as the head position) and return the head of the list. Do nothing if the input position is
 * out of range.
 *
 * Examples:
 *
 * LinkedList: 1->2->3->4 , Head = 1
 *
 * deleteAtMiddle(Head,3) ==> 1->2->4
 */
public class DeleteAtMiddle {

    // horrible, long, stateful solution
    public static ListNode deleteAtMiddle(ListNode head, int position) {
        final ListNode result;
        if (position < 1) {
            throw new IllegalArgumentException("Position must be positive and non-negative");
        } else if (head == null) {
            // empty list
            result = null;
        } else if (position == 1) {
            // delete head
            ListNode next = head.next;
            head.next = null;
            result = next;
        } else {
            position--;
            ListNode previous = head;
            ListNode current = head.next;
            ListNode next = current == null ? null : current.next;
            while (position != 1 && current != null) {
                // ratchet all values to next element
                ListNode tmp = next == null ? null : next.next;
                previous = current;
                current = next;
                next = tmp;
                position--;
            }
            if (current == null) {
                // position was out of bounds; return original list
                result = head;
            } else {
                // link previous to next, skipping current to "delete" it
                previous.next = next;
                result = head;
            }
        }
        return result;
    }




    static class ListNode {
        int data;
        ListNode next;
        ListNode(int data) {
            this.data = data;
        }

        @Override
        public String toString() {
            return "ListNode{" +
                    "data=" + data +
                    ", next=" + next +
                    '}';
        }
    }
}
