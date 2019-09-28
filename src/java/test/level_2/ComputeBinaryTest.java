import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class ComputeBinaryTest {

    @Test
    public void testZero() {
        assertEquals(ComputeBinary.computeBinary(0), "0");
    }

    @Test
    public void testOne() {
        assertEquals(ComputeBinary.computeBinary(1), "1");
    }

    @Test
    public void testFive() {
        assertEquals(ComputeBinary.computeBinary(5), "101");

    }

    @Test
    public void testSix() {
        assertEquals(ComputeBinary.computeBinary(6), "110");
    }
}