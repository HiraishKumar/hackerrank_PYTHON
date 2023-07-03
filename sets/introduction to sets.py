def average(a):
    # your code goes here
    sum=0
    test_set=set(a)
    for i in test_set:
        sum+=i
    return (sum/len(test_set))
