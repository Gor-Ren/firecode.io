import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class CompressStringTest {

    @Test
    public void testEmptyStringReturnsEmpty() {
        assertEquals("", CompressString.compressString(""));
    }

    @Test
    public void testSingleCharNotCompressed() {
        assertEquals(CompressString.compressString("a"), "a");
    }

    @Test
    public void testStringOfUniqueCharsNotCompressed() {
        assertEquals(CompressString.compressString("abc"), "abc");
    }

    @Test
    public void testStringOfNonUniqueNonRepeatingCharsNotCompressed() {
        assertEquals(CompressString.compressString("abab"), "abab");
    }

    @Test
    public void testStringOfOneRepeatingCharCompressed() {
        assertEquals(CompressString.compressString("aaa"), "a3");
    }

    @Test
    public void testStringOfRepeatingCharsCompressed() {
        assertEquals(CompressString.compressString("aabbbcccc"), "a2b3c4");
    }
}
