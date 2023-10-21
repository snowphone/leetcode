class Solution {
    public boolean isMajorityElement(int[] nums, int target) {
        int n = nums.length;
        return bisectRight(nums, target, 0, n) - bisectLeft(nums, target, 0, n) > (n / 2.);
    }

    private int bisectRight(int[] nums, int target, int beg, int end) {
        return bisect(nums, target, beg, end, (trgt, mid) ->  trgt < nums[mid] );
    }
    
    private int bisectLeft(int[] nums, int target, int beg, int end) {
        return bisect(nums, target, beg, end, (trgt, mid) ->  trgt <= nums[mid] );
    }

    /**
     * Bisect left/right는 mid를 버려가는 것이 특징이다.
     */
    private int bisect(int[] nums, int target, int beg, int end, BiFunction<Integer, Integer, Boolean> pred) {
        if (beg >= end) {
            return beg;
        }
        int mid = (beg + end) / 2;
        if (pred.apply(target, mid)) {
            return bisect(nums, target, beg, mid, pred);
        } else {
            return bisect(nums, target, mid + 1, end, pred);
        }
    }
}
