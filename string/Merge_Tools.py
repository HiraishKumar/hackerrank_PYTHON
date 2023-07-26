def merge_the_tools(string, k):
    # your code goes here
    lst=[]
    for i in range((len(string)+1)//k):
        lst.append(string[0+i*k:k+i*k])
    # print(lst)

    for i in lst:
        st=''
        for j in i:
            if j in st:
                pass
            else:
                st+=j
        print(st)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)