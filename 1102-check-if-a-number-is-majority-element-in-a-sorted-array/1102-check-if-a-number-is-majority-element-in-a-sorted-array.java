class Solution {
    public boolean isMajorityElement(int[] nums, int target) {
        int n = nums.length;
        return bisectRight(nums, target, 0, n) - bisectLeft(nums, target, 0, n) > (n / 2.);
    }

    /**
     * Bisect left/right는 mid를 버려가는 것이 특징이다.
     */
    private int bisectRight(int[] nums, int target, int beg, int end) {
        if (beg >= end) {
            return beg;
        }
        int mid = (beg + end) / 2;
        if (target < nums[mid]) {
            return bisectRight(nums, target, beg, mid);
        }  else {
            return bisectRight(nums, target, mid + 1, end);
        }
    }
    private int bisectLeft(int[] nums, int target, int beg, int end) {
        if (beg >= end) {
            return beg;
        }
        int mid = (beg + end) / 2;
        if (nums[mid] < target) {
            return bisectLeft(nums, target, mid+1, end);
        } else {
            return bisectLeft(nums, target, beg, mid);
        }
    }
}
