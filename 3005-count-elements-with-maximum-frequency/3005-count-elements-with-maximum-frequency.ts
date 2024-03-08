function maxFrequencyElements(nums: number[]): number {
	const counter = _(nums)
		.countBy()
		.commit()
	const maxCnt = counter
		.values()
		.max()
	return counter
		.values()
		.filter(it => it == maxCnt)
		.sum()
};