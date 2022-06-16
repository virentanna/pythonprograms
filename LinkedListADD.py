class Solution:
    def __init__(self):
        pass

    def addLinkedLists(self,LL01,LL02):
        sumlist=[]

        LL01 = LL01.head
        LL02 = LL02.head
        Quotient = 0
        while (LL01 != None) | (LL02 != None) | Quotient:
            xSum = 0
            if LL01 != None:
                xSum += LL01.val
            if LL02 != None:
                xSum += LL02.val

            xSum += Quotient
            if (LL01.next != None) | (LL02.next != None):
                sumlist.append(xSum % 10)
            else:
                sumlist.append(xSum)

            Quotient = xSum // 10

            if LL01:
                LL01 = LL01.next
            if LL02:
                LL02 = LL02.next

        print(sumlist)
        return sumlist

class Node:
    def __init__(self,num):
        self.val = num
        self.next = None

class LinkedList:
    def __init__(self,list1):
        for cnt in range(0,len(list1)):
            self.node = Node(list1[cnt])

            if cnt == 0:
                self.head = self.node
                self.last = self.node
                continue

            self.last.next = self.node
            self.last = self.node

    def printList(self):
        xNode = self.head
        while xNode != None:
            print(xNode.val,end=' ---> ')
            xNode = xNode.next
        print(end=' [NONE] \n')

if __name__ == '__main__':
    LL01 = LinkedList([9,7,9,5])
    LL01.printList()

    LL02 = LinkedList([6,5,4])
    LL02.printList()

    SL = Solution()
    sol = SL.addLinkedLists(LL01,LL02)

    LL03 = LinkedList(sol)
    LL03.printList()

