class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=None):
    '''When you define a default argument in a function,
    the default value is evaluated only once, at the time
    of function definition. In this case, EvenStream() 
    would be evaluated once when the function is defined,
    and the same EvenStream instance would be used for 
    every subsequent call to the print_from_stream function.

    This means that if you call print_from_stream(5)
    multiple times, the same EvenStream object will 
    be used for each call. Consequently, the current 
    value of the stream object will keep incrementing 
    from where it left off in the previous call. This 
    can lead to unexpected and undesirable behavior, 
    as the function would not start printing from 0 in 
    every new call.'''
    if stream==None:
        stream=EvenStream()
    for _ in range(n):
        print(stream.get_next())


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
