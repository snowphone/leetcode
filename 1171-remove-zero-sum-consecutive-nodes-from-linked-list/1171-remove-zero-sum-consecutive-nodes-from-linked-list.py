# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def ser(self, head):
        answer = []
        while head:
            answer.append(head.val)
            head = head.next
        return answer

    def psum(self, nums):
        answer = nums[:1]
        for it in nums[1:]:
            answer.append(answer[-1] + it)
        return answer

    def des(self, nums):
        dummy = ListNode()
        node = dummy

        for it in nums:
            node.next = ListNode(it)
            node = node.next
        return dummy.next


    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Prefix sum..?
        '''
        Given psum(i) := sum [0..i]

        sum[...j] - sum[...i] == sum [i+1,j] == 0
        => psum(i) = psum(j) then delete [i+1, j]
        '''
        nums = self.ser(head)
        psum = self.psum(nums)
        print(psum)

        psum_rmap ={0: -1} | {v: i for i, v in enumerate(psum)}
        print(psum_rmap)
        to_delete = set()
        for i in range(-1, len(nums)):
            if i in to_delete:
                continue
            it = psum[i] if i >= 0 else 0
            j = psum_rmap[it]
            if it in psum_rmap and j != i:
                to_delete |= set(range(i+1, j + 1))

        filtered = [it for i, it in enumerate(nums) if i not in to_delete]
        return self.des(filtered)
