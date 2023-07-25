

# Find Nth Node from the End of Linked List

Given a linked list consisting of L nodes and a number N, the task is to find the Nth node from the end of the linked list.

**Example 1:**

**Input:**
N = 2
LinkedList: 1->2->3->4->5->6->7->8->9

**Output: 8**
Explanation: In the first example, there are 9 nodes in the linked list and we need to find the 2nd node from the end. The 2nd node from the end is 8.

**Example 2:**

**Input:**
N = 5
LinkedList: 10->5->100->5

**Output: -1**

Explanation: In the second example, there are 4 nodes in the linked list and we need to find the 5th node from the end. Since 'N' is more than the number of nodes in the linked list, the output is -1.

**Your Task:**
The task is to complete the function `getNthFromLast()` which takes two arguments: reference to the head and N. You need to return the Nth node from the end or -1 in case the node doesn't exist.

**Note:**
Try to solve it in a single traversal.

**Expected Time Complexity: O(N).**

**Expected Auxiliary Space: O(1).**

**Constraints:**
1 <= L <= 10^6
1 <= N <= 10^6