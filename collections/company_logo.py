from collections import Counter
def Func(string):
    con=Counter(sorted(string))
    dic=dict(con.most_common(3))
    for i in dic:
        print(str(i),str(dic[i]))


if __name__ == '__main__':
    s = input()
    Func(s)
