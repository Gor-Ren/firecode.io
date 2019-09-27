/**
 * Compress a sorted String by replacing instances of repeated characters with
 * the character followed by the count of the character.
 *
 * compressString("aaabbbbbcccc") --> a3b5c4
 * compressString("aabbbbccc") --> a2b4c3
 * compressString("abc") --> abc
 */
public class CompressString {

    public static String compressString(String text) {
        if (text.isEmpty() || text.length() == 1) {
            return text;
        }

        StringBuilder result = new StringBuilder();
        char current = text.charAt(0);
        char next;
        int repetitions = 1;
        for (char c : text.substring(1).toCharArray()) {
            next = c;
            if (current == next) {
                repetitions++;
            } else {
                // compress repeated char
                appendCompressed(result, current, repetitions);
                current = next;
                repetitions = 1;
            }
        }
        // append last character(s)
        appendCompressed(result, current, repetitions);
        return result.toString();
    }

    /**
     * Appends the input character to the builder, "compressing" it if it was repeated multiple times.
     *
     * <p>If the character only occurred once ({@code times = 1}) then the char is simply appended. If
     * it occurred {@code n} times in sequence, then the character followed by the number {@code n}
     * is appended.
     *
     * @param builder the string builder to which the compressed character(s) will be appended
     * @param character the character to append
     * @param times the number of times the character was repeated
     * @return the input builder, with the character appended, possibly with compression
     * @throws IllegalArgumentException if {@code times} is zero or negative
     */
    private static StringBuilder appendCompressed(StringBuilder builder, char character, int times) {
        if (times == 1) {
            return builder.append(character);
        } else if (times > 1) { // compress
            return builder.append(character).append(times);
        } else {
            throw new IllegalArgumentException(String.format(
                    "Cannot append char %s negative times [%s]", character, times)
            );
        }
    }
}
