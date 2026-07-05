class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1
        k %= length
        if k == 0: return head
        cur = head
        for _ in range(length - k - 1):
            cur = cur.next
        new_head = cur.next
        cur.next = None
        tail.next = head
        return new_head

