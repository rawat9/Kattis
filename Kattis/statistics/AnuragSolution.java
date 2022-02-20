import java.util.*;

public class AnuragSolution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> nums = new ArrayList<Integer>();
        while (sc.hasNextInt()) {
            int num = sc.nextInt();
            nums.add(num);
        }
        System.out.println(nums);
    }
}
