class Solution {
    subarraySum(arr, n, s) {
        if (s === 0) {
            return [-1];
        }
        let sum2 = arr[0];
        let start = 0;
        let end = 0;

        while (start < n && end < n) {
            if (sum2 === s) {
                return [start + 1, end + 1];
            }
            if (sum2 > s) {
                sum2 -= arr[start];
                start += 1;
            } else {
                end += 1;
                if (end >= n) {
                    return [-1];
                }
                sum2 += arr[end];
            }
        }
        return [-1];
    }
}
