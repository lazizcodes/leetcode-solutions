class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        tortoise = hare = head
        res = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                while tortoise != res:
                    (tortoise, res) = (tortoise.next, res.next)
                return res
        return None