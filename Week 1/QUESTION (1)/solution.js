class Solution {
    minJumps(arr, n) {
        if (n <= 1) {
            return 0;
        }
        if (arr[0] === 0) {
            return -1;
        }
        let reach = arr[0];
        let s = arr[0];
        let j = 1;
        for (let i = 1; i < n; i++) {
            if (i === n - 1) {
                return j;
            }
            reach = Math.max(reach, i + arr[i]);
            s--;
            if (s === 0) {
                if (i >= reach) {
                    return -1;
                }
                j++;
                s = reach - i;
            }
        }
        return -1;
    }
}
