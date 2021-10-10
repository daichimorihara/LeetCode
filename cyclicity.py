"""
Problem: Write a program that takes the head of a singly linked list and returns null
if there does not exist a cycle, and the node at the start of the cycle, if a cycle is present.
"""

def has_cycle(head):
	def cycle_len(end):
		start, step = end, 0
		while True: 
			step += 1
			start = start.next
			if start is end:
				return step

	fast = slow = head
	while fast and fast.next and fast.next.next:
		slow, fast = slow.next, fast.next.next
		if slow is fast:
			# find the start of the cycle
			advanced_it = head
			for _ in range(cycle_len(slow)):
				advanced_it = advanced_it.next

			it = head
			while it is not advanced_it:
				it = it.next
				advanced_it = advanced_it.next
			return it #the start of cycle

	return None #No Cycle




