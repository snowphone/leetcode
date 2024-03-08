function maxFrequencyElements(nums: number[]): number {
	let counter = _(nums)
		.countBy()
		.commit()
	const maxCnt = counter.entries().maxBy(([_, cnt]) => cnt)?.[1] ?? 0
	return counter.entries().filter(([_, cnt]) => cnt == maxCnt).map(([_, cnt]) => cnt).sum()
};