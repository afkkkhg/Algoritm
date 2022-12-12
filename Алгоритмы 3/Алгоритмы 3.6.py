# class Solution(object):
def hasCycle(self, head): # создаем функцию
    slow, fast = head, head
    while fast != None and fast.next != None:  # предоставляю условие на проверку существования строки 6(запись на слд элемент)
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True # вводим значения true и false
    return False