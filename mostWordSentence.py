
def mostWordsFound(self, sentences):
    max=0
    for s in sentences:
        # if len(s.split()) > max:
        #     max = len(s.split())
        max = len(s.split()) if len(s.split()) > max else max
    return max

def newSol(self,sentences):
    return max(len(word.split()) for word in sentences)


if __name__ == '__main__':
    TC01 = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
    TC02 = ["please wait", "continue to fight", "continue to win"]

    print(mostWordsFound(TC01))
    print(newSol(TC01))

