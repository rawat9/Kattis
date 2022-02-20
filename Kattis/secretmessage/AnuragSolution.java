import java.util.Scanner;
import java.util.Arrays;


public class AnuragSolution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int tc = scanner.nextInt();

        for (int i = 0; i < tc; i++) {
            String message = scanner.next();
            int M = (int) Math.sqrt(nextPerfectSquare(message.length()));
            char[] padded = rightPad(message).toCharArray();
        }
        scanner.close();
    }

    static void rotate(int[][] matrix) {

    }

    static String rightPad(String s) {
        int length = nextPerfectSquare(s.length());
        return String.format("%1$-" + length + "s", s).replace(' ', '*');
    }

    static int nextPerfectSquare(int n) {
        int next = (int) Math.floor(Math.sqrt(n)) + 1;
        return next * next;
    }
}
