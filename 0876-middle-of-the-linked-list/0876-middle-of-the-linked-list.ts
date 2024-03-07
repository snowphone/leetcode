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

function middleNode(head: ListNode | null): ListNode | null {
	let it: ListNode|null|undefined = head
	let double = head?.next
	while (double) {
		it = it?.next
		double = double.next?.next
	}
	return it ?? null
};