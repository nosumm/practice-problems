import unittest
from Solution import Node, Solution  # Import from your solution file

class TestCopyRandomList(unittest.TestCase):
    def test_copyRandomList(self):
        # Test case 1: Simple list with random pointers
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node1.next = node2
        node2.next = node3
        node1.random = node3
        node2.random = node1
        node3.random = node2

        sol = Solution()
        copied = sol.copyRandomList(node1)

        # Check values and relationships
        self.assertIsNot(copied, node1)  # Different object
        self.assertEqual(copied.val, node1.val)
        self.assertEqual(copied.next.val, node2.val)
        self.assertEqual(copied.random.val, node3.val)
        self.assertIsNone(sol.copyRandomList(None))  # Edge case: empty list

if __name__ == "__main__":
    unittest.main()