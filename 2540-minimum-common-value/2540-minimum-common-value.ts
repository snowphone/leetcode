function getCommon(nums1: number[], nums2: number[]): number {
	const rhs = new Set(nums2)
	return _(nums1).filter(it => rhs.has(it)).min() ?? -1
};