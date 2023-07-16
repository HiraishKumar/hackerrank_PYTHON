# import calendar
# a=calendar.Calendar()
# print(type(calendar.day_name[i] for i in a.iterweekdays()))


# import calendar
# a = calendar.Calendar()
# print(list(calendar.day_name[i] for i in a.iterweekdays()))


# import calendar

# # Create the calendar object
# cal = calendar.Calendar()

# # Iterate over the weekdays
# for weekday in cal.iterweekdays():
#     print((calendar.day_name[weekday]))


import time
timer=0

for i in range(10):
    start_time = time.time()

    # def first_n(n):
    #     '''Build and return a list'''
    #     num, nums = 0, []
    #     while num < n:
    #         nums.append(num)
    #         num += 1
    #     return nums

    # print(sum(first_n(100000000)))


    # #VS


    # # Using the generator pattern (an iterable)
    # class first_n(object):


    #     def __init__(self, n):
    #         self.n = n
    #         self.num = 0


    #     def __iter__(self):
    #         return self


        
    #     def __next__(self):
    #         return self.next()


    #     def next(self):
    #         if self.num < self.n:
    #             cur, self.num = self.num, self.num+1
    #             return cur
    #         raise StopIteration()


    # print(sum(first_n(100000000)))

    def summer(n):
        num,sum=0,0
        while num<=n:
            sum+=num;
            num+=1
        return sum 
    print(summer(100000000))


    end_time = time.time()
    execution_time = end_time - start_time
    timer+=execution_time

    print("Execution time: ", execution_time, " seconds")
print(timer/10)