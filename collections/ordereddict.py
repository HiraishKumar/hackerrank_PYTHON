# from collections import OrderedDict as od
# mov={'apple':5,'apple':6,'cheese':7,'cheese':8, 'bread':9,'bread':10 }
# test_dict={}
# for item in mov:
#     if item in test_dict:
#         test_dict[item]+=mov[item]
#     else:
#         test_dict[item]=mov[item]
# print(dict(test_dict))
from collections import defaultdict,OrderedDict

mov = [('apple', 5), ('apple', 6), ('cheese', 7), ('cheese', 8), ('bread', 9), ('bread', 10)]
test_dict = defaultdict(int)
odr_dict = OrderedDict()
for item in mov:
    odr_dict[item[0]]=item[1]
for item in mov:
    # print(test_dict[item[0]])
    test_dict[item[0]] += item[1]
    # print(test_dict[item[0]])
for i,j in odr_dict.items():
    print(i,str(j))
