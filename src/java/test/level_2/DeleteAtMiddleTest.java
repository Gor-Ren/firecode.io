import org.junit.Test;

import static org.junit.Assert.*;

public class DeleteAtMiddleTest {

    @Test
    public void testNullSafety() {  // required by challenge test cases
        assertNull(DeleteAtMiddle.deleteAtMiddle(null, 1));
    }

    @Test
    public void testDeleteOutOfRangeDoesNothing() {
        DeleteAtMiddle.ListNode node = new DeleteAtMiddle.ListNode(1);

        DeleteAtMiddle.ListNode result = DeleteAtMiddle.deleteAtMiddle(node, 2);

        assertSame(result, node);
        assertNull(node.next);
    }

    @Test
    public void testDeleteFirstElementFromPair() {
        DeleteAtMiddle.ListNode first = new DeleteAtMiddle.ListNode(1);
        DeleteAtMiddle.ListNode second = new DeleteAtMiddle.ListNode(2);
        first.next = second;

        DeleteAtMiddle.ListNode result = DeleteAtMiddle.deleteAtMiddle(first, 1);

        assertSame(second, result);
    }

    @Test
    public void testDeleteSecondElementFromPair() {
        DeleteAtMiddle.ListNode first = new DeleteAtMiddle.ListNode(1);
        DeleteAtMiddle.ListNode second = new DeleteAtMiddle.ListNode(2);
        first.next = second;

        DeleteAtMiddle.ListNode result = DeleteAtMiddle.deleteAtMiddle(first, 2);

        assertSame(first, result);
        assertNull(first.next);
    }

    @Test
    public void testDeleteMiddleElement() {
        DeleteAtMiddle.ListNode first = new DeleteAtMiddle.ListNode(1);
        DeleteAtMiddle.ListNode middle = new DeleteAtMiddle.ListNode(2);
        DeleteAtMiddle.ListNode last = new DeleteAtMiddle.ListNode(3);
        first.next = middle;
        middle.next = last;
        last.next = null;

        DeleteAtMiddle.ListNode result = DeleteAtMiddle.deleteAtMiddle(first, 2);

        assertSame(first, result);
        assertEquals(first.next, last);
    }
}