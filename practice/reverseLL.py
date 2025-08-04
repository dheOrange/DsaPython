from LL import LinkedList


def reverse(ll):
    temp =ll.head
    ll.head=ll.tail
    ll.tail=temp
    after=temp.next
    before = None
    for _ in range(ll.length):
        after =temp.next
        temp.next=before
        before=temp
        temp=after
ll=LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.append(7)
ll.append(8)
ll.append(9)
ll.append(10)
reverse(ll)
ll.print()
