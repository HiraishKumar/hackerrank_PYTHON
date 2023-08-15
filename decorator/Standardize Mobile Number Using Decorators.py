def wrapper(f):
    def fun(l):
        string=l[-10:-1]      
        f(['+91 ' + string[-10:-5] + ' ' + string[-5:] for string in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
    
