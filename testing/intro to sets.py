n=10
arr=[161,182,161,154,176,170,167,171,170,174]
test_set=set(arr)
def func(a):
    sum=0
    for i in a:
        sum+=i
    return (sum/len(a))
print(func(test_set))
