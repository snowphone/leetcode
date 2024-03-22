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

function toList(head: ListNode | null, acc: number[] = []) {
	if (!head) {
		return acc
	}
	acc.push(head.val)
	return toList(head.next, acc)
}

function isPalindrome(head: ListNode | null): boolean {
	const list = toList(head)
    
	//return _.isEqual(list, list.reverse() )
	return list.toString() === list.reverse().toString()
};