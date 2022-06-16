# Merge 2 SORTED Lists (LeetCode EASY)
# My Solution ---> Solution.MergeLinkedLists()
# 21. Merge Two Sorted Lists

class Node:
    def __init__(self,num=0,next=None):
        self.val = num
        self.next = next

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
        self.node = None

    # def printList(self):
    #     xNode = self.head
    #     while xNode != None:
    #         print(xNode.val,end=' ---> ')
    #         xNode = xNode.next
    #     print(end=' [NONE] \n')

    def printList(self,curr=None):
        xNode = curr
        while xNode != None:
            print(xNode.val, end=' ---> ')
            xNode = xNode.next
        print(end=' [NONE] \n')

    def ExpertSol(self, l1, l2):
        dummy = cur = Node(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2

        return dummy.next


class Solution:
    def __init__(self):
        pass

    def MergeLinkedLists(self,LL01,LL02):
        mergelist=[]

        LL01 = LL01.head if LL01 else None
        LL02 = LL02.head if LL02 else None

        while (LL01 != None) or (LL02 != None):

            if LL01:
                val01 = LL01.val
            else:
                while LL02:
                    mergelist.append(LL02.val)
                    LL02 = LL02.next
                break

            if LL02:
                val02 = LL02.val
            else:
                while LL01:
                    mergelist.append(LL01.val)
                    LL01 = LL01.next
                break

            if val01 < val02:
                mergelist.append(val01)
                if LL01:
                    LL01 = LL01.next
            else:
                mergelist.append(val02)
                if LL02:
                    LL02 = LL02.next

        print(mergelist)
        # return mergelist

if __name__ == '__main__':
    l1 = LinkedList([5,6,9])
    l1.printList()

    l2 = LinkedList([1,2,7])
    l2.printList()

    1,2,5,6,7
    # SL = Solution()
    # sol = SL.MergeLinkedLists(LL01,LL02)

    LL03 = LinkedList([])
    LL03.ExpertSol(l1,l2)
    # LL03.printList()

