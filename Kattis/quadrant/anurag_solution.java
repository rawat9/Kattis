import java.util.Scanner;

public class anurag_solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num1 = sc.nextInt();
        int num2 = sc.nextInt();

        if (num1 > 0 && num2 > 0) {
            System.out.println(1);
        }

        if (num1 < 0 && num2 > 0) {
            System.out.println(2);
        }

        if (num1 < 0 && num2 < 0) {
            System.out.println(3);
        }

        if (num1 > 0 && num2 < 0) {
            System.out.println(4);
        }

        sc.close();
    }
}
