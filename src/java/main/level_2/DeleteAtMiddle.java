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

    public static ListNode deleteAtMiddle(ListNode head, int position) {
        if (position < 1) {
            throw new IllegalArgumentException(
                    "Position must be positive and nonzero: " + position
            );
        } else if (head == null) {
            return null;
        } else if (position == 1) {
            return head.next;
        } else {
            head.next = deleteAtMiddle(head.next, position - 1);
            return head;
        }
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
