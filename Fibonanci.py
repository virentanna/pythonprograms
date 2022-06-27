
def Print_Febonanci(num):
    a=0
    b=1
    idx=1
    while idx <= num:
        print(a,' ',end=' ')
        temp=a
        a,b = a+b,temp
        idx+=1

if __name__ == '__main__':
    Print_Febonanci(5)