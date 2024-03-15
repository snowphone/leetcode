function productExceptSelf(nums: number[]): number[] {
	const zerocnt = nums.filter(it => it == 0).length
	if (zerocnt >= 2) {
		return _.range(nums.length).map(_ => 0)
	} else if (zerocnt == 1) {
		const acc = nums.filter(it => it != 0).reduce((acc, it) => acc * it)
		return nums.map(it => it == 0 ? acc : 0)
	} else {
		const acc = nums.reduce((acc, it) => acc * it)
		return nums.map(it => acc / it)
	}
};