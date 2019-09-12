'''

Flatten any number of nested lists into a single list

'''

#implementation one - use itertools chain.from_iterable method
import itertools


list1d = ["great",[1,2,3],"key",[1,[1,2]]]
list2d = [[1,2,3],[4,5,6], [7], [8,9]]
listOfLists = [[[[[1,2,3,4,5],[10,20,30,40,50],1],100,200,300]]]


# implementation two - use a recursive spread function inside of your deep_flatten
# function function and apply a nested list as an argument.

def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


def deep_flatten(lst):
    result = []
    result.extend(
        spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst))))
    return result
  
# implementation three - use list comprehension - this doesn't flatten all the way

list_comp = [dork for list in listOfLists for dork in list]


merged1 = list(itertools.chain.from_iterable(list1d))
merged2 = list(itertools.chain.from_iterable(list2d))



print(list_comp)
print(deep_flatten(list1d))
print(merged1)
print(deep_flatten(list2d))
print(merged2)
print(list2d)
print(*list2d)
print(list2d[3])
print(*listOfLists)
