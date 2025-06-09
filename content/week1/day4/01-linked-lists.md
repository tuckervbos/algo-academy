# linked lists

## linked lists

- linked lists are made up of "list nodes"
- each of these nodes encapsulate at minimum 2 components

  - value
  - pointers to other nodes
    - next pointer
    - prev pointer (for doubly linked list)
  - we can represent these nodes using objects with key-value pairs
    - example:
      - {
        value: 0,
        next: NODE,
        prev: NODE
        }

- 1 -> 2 -> 3 -> || <- 1 <=> 2 <=> 3 -> (doubly linked)
  {
  val: 1
  next: 2
  }
  {
  val: 2
  next: 3
  }
  {
  val 3:
  next: ..
  }

## singly linked lists

- [singly-linked-lists](/content/week1/day4/01.1-singly-linked-lists.png)
- [singly-linked-lists](/content/week1/day4/01.2-singly-linked-lists.png)

## chaining .next

- from ListNode1, we can access ListNode2 by using ListNode1.next
- we can access ListNode3 from both ListNode1 or ListNode2 with the following:
  - ListNode1.next.next
  - ListNode2.next

## doubly linked lists

- ListNode { prev | value | next }

- ListNode1 {
  prev:
  value: red
  next:
- }
  <=>
- ListNode2 {
  prev:
  value: blue
  next:
- }
  <=>
- ListNode3 {
  prev:
  value: green
  next:
- }

## how do we traverse a linked list?

- iterative:

```python
def traverse(head):
  current = head
  while (current):
    current = current.next
  return None
```

- recursive:

```python
def traverse(head):
  if not head:
    return None
  return traverse(head.next)
```

## linked list runtimes

- operations | big O time

- read / write ith element | O(n)
- insert / remove end | O(1) (assuming there is a tail)
- insert middle or beginning | O(1)
- remove middle or beginning | O(1)

## comparing with array runtimes

- [comparing-array-runtimes](/content/week1/day4/01.3-comparing-array-runtimes.png)
- LRUcache problem - great example of linked list implementation

## demos

- [middle of the linked list](https://leetcode.com/problems/middle-of-the-linked-list/description/)
- [reverse linked list](https://leetcode.com/problems/reverse-linked-list/description/)
