import java.util.*;
import java.io.*;

class Main {

    private static char[] reversed(char[] arr) {
        char[] newArr = new char[arr.length];
        int index = 0;
        for (int i = arr.length - 1; i >= 0; i--) {
            newArr[index] = arr[i];
            index++;
        }
        return newArr;
    }

    private static int arrToNum(char[] arr) {
        String s = "";
        for (char c : arr) {
            s += c;
        }
        return Integer.parseInt(s);
    }

    public static int KaprekarsConstant(int num) {

        char[] chars = ("" + num).toCharArray();
        Arrays.sort(chars); // sort ascending
        char[] reversedArr = reversed(chars);

        int target = 6174;
        int count = 0;
        int current = 0;

        while (current != target) {
            int asc = arrToNum(chars);
            int desc = arrToNum(reversedArr);
            if (asc > desc) {
                current = asc - desc;
            } else {
                current = desc - asc;
            }
            count++;
            chars = ("" + current).toCharArray();
            Arrays.sort(chars); // sort ascending
            reversedArr = reversed(chars);
        }
        return count;

    }

    public static void main(String[] args) {
        // keep this function call here     
        Scanner s = new Scanner(System.in);
        System.out.print(KaprekarsConstant(s.nextLine()));
    }

}
