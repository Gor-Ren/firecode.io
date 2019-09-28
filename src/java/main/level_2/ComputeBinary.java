import java.math.BigInteger;
import java.util.Arrays;

/**
 * Write a method to compute the binary representation of a positive integer.
 * The method should return a string with 1s and 0s.
 *
 * computeBinary(6) ==> "110"
 * computeBinary(5) ==> "101"
 */
public class ComputeBinary {

    public static String computeBinary(int val) {
        return trimLeadingZeroes(
                Integer.toBinaryString(val)
        );
    }

    /**
     * Returns a substring of the input with all leading {@code '0'} chars removed.
     *
     * <p>{@code "01" -> "1"}
     * <p>{@code "00010" -> "10"}
     * <p>{@code "0" -> "0"}, a special case; the '0' is not considered leading
     * <p>{@code "1" -> "1"}
     *
     * @param input the string from which zeroes will be trimmed.
     * @return a substring of the input, beginning from the first non-zero char.
     */
    private static String trimLeadingZeroes(String input) {
        int numLeadingZeroes = 0;
        for (char c : input.toCharArray()) {
            if (c == '0') {
                numLeadingZeroes++;
            } else {
                break;
            }
        }

        if (numLeadingZeroes == 0) {
            return input;
        } else if (input.equals("0")) {
            return input;
        } else {
            return input.substring(numLeadingZeroes);
        }
    }
}
