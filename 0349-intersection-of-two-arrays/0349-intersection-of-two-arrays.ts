function intersection(nums1: number[], nums2: number[]): number[] {
	const lhs = new Set(nums1)
	const rhs = new Set(nums2)

    return _(lhs).toArray().filter(it => rhs.has(it)).toArray().value()
};