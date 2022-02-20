import java.util.Arrays;
import java.util.Scanner;

public class AnuragSolution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        String[] numbers = input.split(" ");

        int[] array = new int[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            array[i] = Integer.parseInt(numbers[i]);
        }

        int n = array[0];
        int k = array[1];
        double max, min;
        int overall = 0;

        for (int j = 0; j < k; j++) {
            int rating = scanner.nextInt();
            overall += rating;
        }

        max = (double) (overall + 3 * (n - k)) / n;
        min = (double) (overall + (-3) * (n - k)) / n;

        System.out.println(min + " " + max);
    }
}
