import java.util.Arrays;
import java.util.Scanner;

public class AnuragSolution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        for (int i = 0; i < n; i++) {
            int k = scanner.nextInt();
            int[] sequence = new int[k];

            for (int j = 0; j < k; j++)
                sequence[j] = scanner.nextInt();

            boolean result = isArithmetic(sequence);
            Arrays.sort(sequence);
            boolean sorted = isArithmetic(sequence);
            if (result) System.out.println("arithmetic");
            else if (sorted) System.out.println("permuted arithmetic");
            else System.out.println("non-arithmetic");
        }
        scanner.close();
    } 

    public static boolean isArithmetic(int[] sequence) {
        boolean isValid = true;
        int diff = sequence[1] - sequence[0];

        for (int i = 0; i < sequence.length - 1; i++) {
            if (sequence[i+1] - sequence[i] != diff) {
                isValid = false;
            }
        }
        return isValid;
    }
}
