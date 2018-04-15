
/*

Description:
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

Max.sequence(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4});
// should be 6: {4, -1, 2, 1}
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

*/

import java.util.stream.*;

public class Max {
    public static int sequence(int[] arr) {
        // empty array is sum of zero or no positive values should be a sum of 0
        if (arr.length == 0 || IntStream.of(arr).allMatch(i -> i <= 0)) {
            return 0;
        }

        // all positive should be the sum of all elements
        if (IntStream.of(arr).allMatch(i -> i > 0)) {
            return IntStream.of(arr).sum();
        }

        int maxSum = 0;

        for (int i = 0; i < arr.length; i++) {
            int currSum = 0;
            for (int j = i; j < arr.length; j++) {
                currSum += arr[j];
                if (currSum > maxSum) {
                    maxSum = currSum;
                }
            }
        }

        return maxSum;
    }
}