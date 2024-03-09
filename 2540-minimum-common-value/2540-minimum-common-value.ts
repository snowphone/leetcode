function getCommon(nums1: number[], nums2: number[]): number {
	function findFirst(i: number, j: number) {
		if (i == nums1.length || j == nums2.length) {
			return -1
		}
		const [lhs, rhs] = [nums1[i], nums2[j]]

		if (lhs < rhs) {
			return findFirst(i + 1, j)
		} else if (lhs > rhs) {
			return findFirst(i, j + 1)
		}
		return lhs
	}
	return findFirst(0, 0)
};