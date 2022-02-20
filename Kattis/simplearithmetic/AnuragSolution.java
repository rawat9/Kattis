import java.util.Scanner;

public class anurag_solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] arr = sc.nextLine().split(" ");
            
        int[] nums = new int[3];
        for (int i = 0; i < 3; i++) {
            nums[i] = Long.parseLong(arr[i]);
        }

        double result = nums[0] * (double) nums[1] / nums[2];
        System.out.println(result);
    }
}
