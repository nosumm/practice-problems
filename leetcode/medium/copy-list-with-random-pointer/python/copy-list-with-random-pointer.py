# Solution for copy-list-with-random-pointer (Python)
# Problem: https://leetcode.com/problems/copy-list-with-random-pointer/

class Solution(object){
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        # copy the values into new linked list
        mapping = {}
        current = head
        while current:
            mapping[current] = Node(current.val)
            current = current.next
        
        current = head 

        # assign next and random pointers in the new copied list
        current = head
        while current:
            if current.next:
                mapping[current].next = mapping[current.next]
            if current.random:
                mapping[current].random = mapping[current.random]
            current = current.next 
        return mapping[head]

}

