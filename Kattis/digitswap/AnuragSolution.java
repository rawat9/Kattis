import java.util.Scanner;

class AnuragSolution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        int firstDigit = num % 10;
        int secondDigit = num / 10;

        System.out.println(firstDigit * 10 + secondDigit);
        sc.close();
    }
}
