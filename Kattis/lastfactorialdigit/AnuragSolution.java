import java.util.Scanner;

public class AnuragSolution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int tc = scanner.nextInt();

        for (int i = 0; i < tc; i++) {
            int n = scanner.nextInt();
            int lastDigit = factorial(n) % 10;
            System.out.println(lastDigit);
        }
    }

    static int factorial(int n) {
        int fact = 1;
        for (int num = 2; num < n+1; num++) {
            fact *= num;
        }
        return fact;
    }

}
