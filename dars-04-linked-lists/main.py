"""
Ma'lumotlar tuzilmasi va algoritmlar

#05-LINKED LISTS

Muallif: Anvar Narzullaev

Web sahifa: https://t.me/sariq.dev
"""

from linkedlistfuncs import Node, LinkedList

## Linked List yaratamiz
llist = LinkedList()

## Uchta node (tugun) yaratamiz
llist.head = Node('Dushanba')
tuesday = Node('Seshanba')
wednesday = Node('Chorshanba')

## Tugunlarni bog'laymiz
llist.head.next = tuesday
tuesday.next = wednesday

## Linked Listni konsolga chiqaramiz:
# llist.printList()

## List boshiga yangi tugun qo'shamiz
llist.push('Yakshanba')
# llist.printList()

## List o'rtasiga element qo'shamiz
# llist.insertAfter(llist.head.next.next, 'Seshanba Kechasi')
# llist.printList()

## List oxiriga tugun qo'shamiz
llist.append('Payshanba')
llist.append('Juma')
# llist.printList()

## Element o'chiramiz
llist.deleteNode('Seshanba')
llist.printList()