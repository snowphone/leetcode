function getCommon(nums1: number[], nums2: number[]): number {
	const cmp = (i: number, j: number) => {
		if (i == nums1.length || j == nums2.length) {
			return -1
		}
		const [lhs, rhs] = [nums1[i], nums2[j]]

		if (lhs < rhs) {
			return cmp(i + 1, j)
		} else if (lhs > rhs) {
			return cmp(i, j + 1)
		}
		return lhs
	}

	return cmp(0, 0)
};