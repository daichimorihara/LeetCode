"""
Implement a function to check if a linked list is a palindrome.
"""

def solution(ll):
	fast = slow = ll.head
	stack = []
	while fast and fast.next:
		stack.append(slow.value)
		slow = slow.next
		fast = fast.next.next

	if fast: 
		slow = slow.next

	while slow:
		top = stack.pop()
		if top != slow.value:
			return False

		slow = slow.next

	return True