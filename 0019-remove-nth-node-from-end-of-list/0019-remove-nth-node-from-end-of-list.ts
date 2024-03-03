/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function len(head: ListNode | null): number {
	let sz = 0
	while (!!head) {
		sz += 1
		head = head.next
	}
	return sz
}

function remove(head: ListNode | null, nth: number): ListNode | null {
	const dummy = new ListNode(-1, head)
	let [prev, it]: [ListNode | null, ListNode | null] = [dummy, head]

	for (let _ = 0; _ < nth; _++) {
		[prev, it] = [it, it!!.next]
	}
	prev!!.next = it!!.next
	return dummy.next
}

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
	const sz = len(head)
	const nth = sz - n

	return remove(head, nth)
};