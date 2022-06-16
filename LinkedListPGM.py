class Solution:
    def __init__(self):
        pass

    def addLinkedLists(self,LL01,LL02):
        sumlist=[]
        quotient =  0

        LL01 = LL01.head
        LL02 = LL02.head

        while (LL01!=None) | (LL02!=None) :
            val01,val02,rem = 0,0,0
            if LL01:
                val01 = LL01.val
                LL01 = LL01.next
            if LL02:
                val02 = LL02.val
                LL02 = LL02.next

            sum = val01 + val02 + quotient
            rem = sum % 10

            if (LL01 == None) & (LL02 == None):
                sumlist.append(sum)
                return sumlist

            sumlist.append(rem)
            quotient = sum // 10

class Node:
    def __init__(self,num):
        self.val = num
        self.next = None

class LinkedList:
    def __init__(self,list1):
        if len(list1) > 0:
            for cnt in range(0,len(list1)):
                self.node = Node(list1[cnt])

                if cnt == 0:
                    self.head = self.node
                    self.last = self.node
                    continue

                self.last.next = self.node
                self.last = self.node
        else:
            self.head=None

    def printList(self):
        if self.head == None:
            print("Empty List..")
            return
        xNode = self.head
        while xNode != None:
            print(xNode.val,end=' ---> ')
            xNode = xNode.next
        print(end=' [NONE] \n')

if __name__ == '__main__':
    LL01 = LinkedList([])
    LL01.printList()

    LL02 = LinkedList([0,1])
    LL02.printList()

    SL = Solution()
    sol = SL.addLinkedLists(LL01,LL02)

    LL03 = LinkedList(sol)
    LL03.printList()

