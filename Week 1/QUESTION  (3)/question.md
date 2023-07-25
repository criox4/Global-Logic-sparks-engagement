# Remove loop in Linked List

Given a linked list of N nodes that may contain a loop. A loop in this context means that the last node of the linked list is connected to a node at position X (1-based index). If the linked list does not have any loop, X=0. The task is to remove the loop from the linked list, if it is present, i.e., unlink the last node that is forming the loop.

**Example 1:**

**Input:**
N = 3
value[] = {1,3,4}
X = 2

Output: 1

Explanation: The linked list looks like:

1 -> 3 -> 4
     ^    |
     |____|    
A loop is present. If you remove it successfully, the answer will be 1. 

**Example 2:**

**Input:**
N = 4
value[] = {1,8,3,4}
X = 0
Output: 1
Explanation: The linked list does not contain any loop.

**Example 3:**

**Input:**
N = 4   
value[] = {1,2,3,4}
X = 1
Output: 1
Explanation: The linked list looks like:
1 -> 2 -> 3 -> 4
^              |
|______________|
A loop is present. If you remove it successfully, the answer will be 1. 

Your Task:
You don't need to read input or print anything. Your task is to complete the function `removeLoop()` which takes the head of the linked list as the input parameter. Simply remove the loop in the list (if present) without disconnecting any nodes from the list.

Note: The generated output will be 1 if your submitted code is correct.

Expected time complexity: O(N)
Expected auxiliary space: O(1)

Constraints:
1 ≤ N ≤ 10^4