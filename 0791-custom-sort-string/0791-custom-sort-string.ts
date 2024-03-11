function customSortString(order: string, s: string): string {
	const ord = order
		.split('')
		.map((v, i) => ({v, i}))
		.reduce((acc, {v, i}) => acc.set(v, i), new Map<string, number>())
	const sorter = (it: string) => ord.get(it) ?? 999

	return _(s)
		.split('')
		.sortBy(sorter)
		.toArray()
		.join('')
};